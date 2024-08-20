import json
from typing import Any
import requests as req
from requests.auth import AuthBase

from singleton import Singleton

class TokenAuth(AuthBase):
    """Присоединяет HTTP аутентификацию к объекту запроса."""
    def __init__(self, token, id):
        # здесь настроем любые данные, связанные с аутентификацией 
        self.token = token
        self.id = id

    def __call__(self, req):
        # изменяем и возвращаем запрос
        if self.token:
            req.headers['X-Id'] = self.id
            req.headers['X-Auth'] = self.token
        return req

class SkudApiRequsts(Singleton):
    def __init__(self, url: str, id) -> None:
        self.url = url
        self.id = id
        self.token_auth = None
        self.requests = { "get"   : req.get, 
                          "post"  : req.post,
                          "put"   : req.put,
                          "delete": req.delete }

    def request(self, type: str, body: Any, path="") -> req.Response | None:
        try:
            response = self.requests[type](self.url+path, data=body, auth=self.token_auth)
            if response.status_code == 200:
                return response
            else:
                print(f"Ошибка {response.status_code}: {response.reason}")
        except Exception as error:
            print("get ERR", error)

    def fmt(self, data) -> dict:
        return { "data"  : json.dumps(data) }
    
    def get_table(self, table: str, start: int, order_column: str, order_type: bool) -> dict | None:
        # start = -1 означает, что требуется предоставить все записи
        # -----------------------------Для тестов-----------------------------
        return {'data': [], 'error': ''}
        # -----------------------------Для тестов-----------------------------

        data = {"start"       : start, 
                "order_type"  : order_type, 
                "order_column": order_column}
 
        response = self.get(self.fmt(data), f"/ui/{table}")
        try: 
            return response.json()
        except Exception as error:
            print("response:", response.text if response else "None", 
                  "ERR:", error)
            
    def get_rights(self, getall=False):
        return self.get(self.fmt({"all": getall}), "/ui/rights")
    
    def authentication(self, key: int) -> tuple[bool, str]:
        data = json.dumps({"key": key, "id": self.id})
        response = self.get({"auth": data}, "/auth")
        try:
            answer = response.json()
            print(answer)

            err = "answer is None"
            if answer:
                err = answer["error"]
                if err == "":
                    self.token_auth = TokenAuth(answer["data"], self.id)
                    return True, err
            return False, err
        except BaseException as error:
            return False, error
            
    def add_row(self, table: str, values: dict) -> bool:
        return self.request("post", self.fmt(values), f"/ui/{table}")

    def check_order(self, table: str, data: dict):
        # AUTOMATA : Зачем эта штука нужна ??
        pass

    def edit_order(self, table: str, id: Any, new_values: dict):
        data = self.fmt({"key": id, "values": new_values})
        return self.request("post", data, f"/ui/{table}")

    def delete_order(self, table: str, id):
        data = self.fmt({"key": id})
        return self.request("delete", data, f"/ui/{table}")

    def authentication(self, key: int) -> tuple[bool, str]:
        data = json.dumps({"key": key, "id": self.id})
        response = self.get({"auth": data}, "/auth")
        try:
            answer = response.json()
            err = "answer is None"
            if answer:
                err = answer["error"]
                if err == "":
                    self.token = answer["data"]
                    return True, err
            return False, err
        except BaseException as error:
            return False, error

