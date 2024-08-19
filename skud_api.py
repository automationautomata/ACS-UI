import json
from typing import Any
import requests
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
        req.headers['X-Id'] = self.id
        req.headers['X-Auth'] = self.token
        return req

class SkudApiRequsts(Singleton):
    
    def __init__(self, url: str, id: int) -> None:
        self.url = url
        self.token = None
        self.id = id

    def get(self, body: Any, path="") -> requests.Response | None:
        try:
            auth = TokenAuth(self.token, self.id) if self.token else None

            response = requests.get(self.url+path, data=body, auth=auth)
            if response.status_code == 200:
                return response
            else:
                print(f"Ошибка {response.status_code}: {response.reason}")
        except BaseException as error:
            print("get ERR", error)

    def fmt(self, action, data) -> dict:
        return {"action": action, 
                "data"  : json.dumps(data)}
    
    def get_table(self, table: str, start: int, sorting_rules: dict) -> dict | None:
        # start = -1 означает, что требуется предоставить все записи
        # -----------------------------Для тестов-----------------------------
        return {'data': [], 'error': ''}
        # -----------------------------Для тестов-----------------------------

        action = f"{table} query"
        data = {"start"       : start, 
                "sorting_rules"  : sorting_rules}
 
        response = self.get(self.fmt(action,  data), "/ui")
        try: 
            return response.json()
        except BaseException as error:
            print("response:", response.text if response else "None", "ERR:", error)
        
    def add_order(self, table: str, data: dict) -> bool:
        pass

    def check_order(self, table: str, data: dict):
        pass

    def edit_order(self, table: str, id, new_data: dict):
        pass

    def delete_order(self, table: str, id):
        pass

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

