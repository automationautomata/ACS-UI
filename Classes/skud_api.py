import json
from typing import Any
import requests as req
from requests.auth import AuthBase

#from Classes.singleton import Singleton

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

class SkudApiRequests():
    def __init__(self, url: str, id: int) -> None:
        self.url = url
        self.id = id
        self.table_sorting_rules = {'entities_view': {'column': 'card',
                                        'rule': 'default',
                                        'deleted_record': False},
                                    'access_rules_view': {'column': 'room',
                                        'rule': 'default',
                                        'deleted_record': False},
                                    'cards': {'column': 'id',
                                        'rule': 'default',
                                        'deleted_record': False},
                                    'rooms': {'column': 'id',
                                        'rule': 'default',
                                        'deleted_record': False},
                                    'rights': {'column': 'id',
                                        'rule': 'default',
                                        'deleted_record': False}}
        self.token_auth = None
        self.requests = { "get"   : req.get, 
                          "post"  : req.post,
                          "put"   : req.put,
                          "delete": req.delete }

    def request(self, type: str, body: Any, path="", headers=None): #-> req.Response | None:
        try:
            response = self.requests[type](self.url+path, data=body, auth=self.token_auth, headers=headers)
            if response.status_code == 200:
                return response
            else:
                print(f"Ошибка {response.status_code}: {response.reason}")
        except Exception as error:
            print("get ERR", error)

    def fmt(self, arg_name, data) -> dict:
        return { arg_name  : json.dumps(data) }
    
    def switch_sorting_rules(self, table: str, column: str | None=None, deleted_record: bool | None=None) -> None:
        def next_rule(rule):
            if rule == 'default':
                return 'A-Z'
            elif rule == 'A-Z':
                return 'Z-A'
            else:
                return 'default'
        if deleted_record is None:
            if self.table_sorting_rules[table]['column'] == column:
                self.table_sorting_rules[table]['rule'] = next_rule(self.table_sorting_rules[table]['rule'])
            else:
                self.table_sorting_rules[table]['column'] = column
                self.table_sorting_rules[table]['rule'] = 'default'
                self.table_sorting_rules[table]['rule'] = next_rule(self.table_sorting_rules[table]['rule'])
            #self.check()
            return self.table_sorting_rules[table]['rule']
        elif column is None:
            self.table_sorting_rules[table]['deleted_record'] = deleted_record
            #self.check()


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

    def get_table(self, table: str, start: int): #-> dict | None:
    #def get_table(self, table: str, start: int, order_column: str, order_type: bool) -> dict | None:
        # start = -1 означает, что требуется предоставить все записи
        # -----------------------------Для тестов-----------------------------
        #return {'data': [], 'error': ''}
        # -----------------------------Для тестов-----------------------------

        # data = {"start"       : start, 
        #         "sorting_rules"  : self.table_sorting_rules[table]}
        #        "order_type"  : order_type, 
        #        "order_column": order_column}
        sorting_rules = self.table_sorting_rules[table]
        data = {"start"       : start, 
                "order_type"  : sorting_rules["rule"],
                "order_column": sorting_rules["column"]}
        response = self.request("get", self.fmt("params", data), f"/ui/{table}", headers={"NULL": str(sorting_rules["deleted_record"])})
        try: 
            return response.json()
        except Exception as error:
            print("response:", response.text if response else "None", 
                  "ERR:", error)
            
    def get_rights(self, getall=False):
        return self.request("get", self.fmt({"all": getall}), "/ui/rights")
    
    def authentication(self, key: int) -> tuple[bool, str]:
        data = json.dumps({"key": key, "id": self.id})
        response = self.request("get", {"auth": data}, "/auth")
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
        response = self.request("get", {"auth": data}, "/auth")
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

