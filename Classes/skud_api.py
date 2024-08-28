import json
from typing import Any
import requests as req
from requests.auth import AuthBase

from Classes.singleton import Singleton

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
<<<<<<< HEAD:Classes/skud_api.py
    def __init__(self, url: str, id: int) -> None:
=======
    def __init__(self, url: str, id) -> None:
>>>>>>> 804de74623ff3ac279e0624ff0b4deab47d402a9:skud_api.py
        self.url = url
        self.id = id
<<<<<<< HEAD:Classes/skud_api.py
        self.table_sorting_rules = {'entities_view': {'column': '',
                                        'rule': '',
                                        'deleted_record': False},
                                    'access_rules_view': {'column': '',
                                        'rule': '',
                                        'deleted_record': False},
                                    'cards': {'column': '',
                                        'rule': '',
                                        'deleted_record': False},
                                    'rooms': {'column': '',
                                        'rule': '',
                                        'deleted_record': False},
                                    'rights': {'column': '',
                                        'rule': '',
                                        'deleted_record': False}}
=======
        self.token_auth = None
        self.requests = { "get"   : req.get, 
                          "post"  : req.post,
                          "put"   : req.put,
                          "delete": req.delete }
>>>>>>> 804de74623ff3ac279e0624ff0b4deab47d402a9:skud_api.py

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
    
<<<<<<< HEAD:Classes/skud_api.py
    def switch_sorting_rules(self, table: str, column: str) -> None:
        pass

    def switch_sorting_rules(self, table: str, deleted_record: bool) -> None:
        self.table_sorting_rules[table]['deleted_record'] = deleted_record


    def check(self):
        print('--------')
        print('-------------------')
        print('-----------------------------')
        for table in self.table_sorting_rules.keys():
            print(table)
            print('   column: ', self.table_sorting_rules[table]['column'])
            print('   rule: ', self.table_sorting_rules[table]['rule'])
            print('   deleted_record: ', self.table_sorting_rules[table]['deleted_record'])
            print('-----------------------------')


    def get_sorting_rules(self, table: str) -> dict:
        return self.table_sorting_rules[table]

    def get_table(self, table: str, start: int) -> dict | None:
=======
    def get_table(self, table: str, start: int, order_column: str, order_type: bool) -> dict | None:
>>>>>>> 804de74623ff3ac279e0624ff0b4deab47d402a9:skud_api.py
        # start = -1 означает, что требуется предоставить все записи
        # -----------------------------Для тестов-----------------------------
        return {'data': [], 'error': ''}
        # -----------------------------Для тестов-----------------------------

        data = {"start"       : start, 
<<<<<<< HEAD:Classes/skud_api.py
                "sorting_rules"  : self.table_sorting_rules[table]}
=======
                "order_type"  : order_type, 
                "order_column": order_column}
>>>>>>> 804de74623ff3ac279e0624ff0b4deab47d402a9:skud_api.py
 
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

<<<<<<< HEAD:Classes/skud_api.py
    def check_order(self, table: str, data: dict) -> bool:
        pass

    def edit_order(self, table: str, id, new_data: dict) -> bool:
        pass

    def delete_order(self, table: str, id) -> bool:
        pass
=======
    def check_order(self, table: str, data: dict):
        # AUTOMATA : Зачем эта штука нужна ??
        pass

    def edit_order(self, table: str, id: Any, new_values: dict):
        data = self.fmt({"key": id, "values": new_values})
        return self.request("post", data, f"/ui/{table}")

    def delete_order(self, table: str, id):
        data = self.fmt({"key": id})
        return self.request("delete", data, f"/ui/{table}")
>>>>>>> 804de74623ff3ac279e0624ff0b4deab47d402a9:skud_api.py

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





