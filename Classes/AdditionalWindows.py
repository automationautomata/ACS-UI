import kivy
import Classes.Buttons
kivy.require('1.9.0')

import Classes.Buttons as btn

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox

from kivy.graphics import Color, Rectangle, Line, Triangle
from kivy.properties import StringProperty, ListProperty, NumericProperty

global app


class DomainWindow(Popup):
    def __init__(self, **kwargs):
        super(DomainWindow, self).__init__(**kwargs)

    def open_win(self) -> None:
        ''''''
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.domain_menu()

    def domain_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self.ids.main_area.add_widget(btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self))

class FindWindow(Popup):
    def __init__(self, **kwargs):
        super(FindWindow, self).__init__(**kwargs)

    def open_win(self, entity):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self._entity = entity

        self.open()

    def on_open(self):
        self.find_menu()

    def find_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self.ids.main_area.add_widget(btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self))

        if self._entity == 'cards':
            self.menu_card()
        elif self._entity == 'rooms':
            self.menu_room()
        elif self._entity == 'rights':
            self.menu_right()
        elif self._entity == 'entities_view':
            self.menu_link()
        elif self._entity == 'access_rules_view':
            self.menu_rule()

    def menu_card(self):
        self._result = {}

        self._result['card_id_label'] = Label(text='Id',
            pos=(75, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['card_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 175),
            size_hint=(None, None),
            size=(250, 35))
        self._result['card_label'] = Label(text='Card number',
            pos=(75, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 275),
            size_hint=(None, None),
            size=(250, 35))
        
        self._result['card_sabotaget_label'] = Label(text='Is sabotaget:',
            pos=(75, self.height - 325),
            size_hint=(None, None),
            size=(100, 15))
        self._result['card_sabotaget_result'] = CheckBox(pos=(200, self.height - 325),
            size_hint=(None, None),
            size=(15, 15))

        self._result['card_was_added_label'] = Label(text='Date the card was added',
            pos=(400, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['card_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))
        self._result['card_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))

        self._result['card_was_deleted_label'] = Label(text='Date the card was deleted',
            pos=(400, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['card_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['card_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}

        self._result['room_id_label'] = Label(text='Id',
            pos=(75, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['room_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 175),
            size_hint=(None, None),
            size=(250, 35))
        self._result['room_label'] = Label(text='Name of room',
            pos=(75, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['room_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 275),
            size_hint=(None, None),
            size=(250, 35))
        
        self._result['room_was_added_label'] = Label(text='Date the room was added',
            pos=(400, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['room_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))
        self._result['room_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))

        self._result['room_was_deleted_label'] = Label(text='Date the room was deleted',
            pos=(400, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['room_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['room_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}

        self._result['right_id_label'] = Label(text='Id',
            pos=(75, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['right_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 175),
            size_hint=(None, None),
            size=(250, 35))
        self._result['right_label'] = Label(text='Name of right',
            pos=(75, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['right_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(75, self.height - 275),
            size_hint=(None, None),
            size=(250, 35))
        
        self._result['right_was_added_label'] = Label(text='Date the right was added',
            pos=(400, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['right_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 175),
            size_hint=(None, None),
            size=(95, 35))

        self._result['right_was_deleted_label'] = Label(text='Date the right was deleted',
            pos=(400, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['right_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(425, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(530, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}

        self._result['link_id_label'] = Label(text='Link id',
            pos=(45, self.height - 100),
            size_hint=(None, None),
            size=(175, 15))
        self._result['link_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(45, self.height - 150),
            size_hint=(None, None),
            size=(175, 35))
        self._result['entity_name_label'] = Label(text='sid',
            pos=(45, self.height - 175),
            size_hint=(None, None),
            size=(175, 15))
        self._result['entity_name_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(45, self.height - 225),
            size_hint=(None, None),
            size=(175, 35))
        self._result['type_label'] = Label(text='Type',
            pos=(45, self.height - 250),
            size_hint=(None, None),
            size=(175, 15))
        type_dropdown = DropDown()
        # Запрос: список всех типов из бд
        list_of_type = app.requsts_controller.get_table(table='types', start=-1)['data']
        list_of_type = [{'name': 'Type 1'}, {'name': 'Type 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_type) > 0:
            for _type in list_of_type:
                button = btn.TipButton(text=_type['name'],
                    size_hint=(None, None),
                    height=35,
                    width=175,
                    valign='center',
                    halign='center',
                    visible_symb=12)
                button.bind(on_press_event=lambda button:type_dropdown.select(button))
                type_dropdown.add_widget(button)
        self._result['type_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(45, self.height - 300),
            size_hint=(None, None),
            size=(175, 35))
        self._result['type_result'].bind(on_release=type_dropdown.open)
        type_dropdown.bind(on_select=lambda instance, x: setattr(self._result['type_result'], 'text', x.text))
        type_dropdown.bind(on_select=lambda instance, x: x.on_leave())
        self._result['entity_was_added_label'] = Label(text='Date the entity was added',
            pos=(32.5, self.height - 340),
            size_hint=(None, None),
            size=(200, 15))
        self._result['entity_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(32.5, self.height - 390),
            size_hint=(None, None),
            size=(95, 35))
        self._result['entity_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(137.5, self.height - 390),
            size_hint=(None, None),
            size=(95, 35))
        self._result['entity_was_deleted_label'] = Label(text='Date the entity was deleted',
            pos=(32.5, self.height - 430),
            size_hint=(None, None),
            size=(200, 15))
        self._result['entity_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(32.5, self.height - 480),
            size_hint=(None, None),
            size=(95, 35))
        self._result['entity_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(137.5, self.height - 480),
            size_hint=(None, None),
            size=(95, 35))

        self._result['card_id_label'] = Label(text='Card id',
            pos=(295, self.height - 100),
            size_hint=(None, None),
            size=(175, 15))
        self._result['card_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(295, self.height - 150),
            size_hint=(None, None),
            size=(175, 35))
        self._result['card_label'] = Label(text='Card number',
            pos=(295, self.height - 175),
            size_hint=(None, None),
            size=(175, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(295, self.height - 225),
            size_hint=(None, None),
            size=(175, 35))
        self._result['card_sabotaget_label'] = Label(text='Is sabotaget:',
            pos=(295, self.height - 280),
            size_hint=(None, None),
            size=(110, 15))
        self._result['card_sabotaget_result'] = CheckBox(pos=(420, self.height - 280),
            size_hint=(None, None),
            size=(15, 15))
        self._result['card_was_added_label'] = Label(text='Date the card was added',
            pos=(282.5, self.height - 340),
            size_hint=(None, None),
            size=(200, 15))
        self._result['card_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(282.5, self.height - 390),
            size_hint=(None, None),
            size=(95, 35))
        self._result['card_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(387.5, self.height - 390),
            size_hint=(None, None),
            size=(95, 35))
        self._result['card_was_deleted_label'] = Label(text='Date the card was deleted',
            pos=(282.5, self.height - 430),
            size_hint=(None, None),
            size=(200, 15))
        self._result['card_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(282.5, self.height - 480),
            size_hint=(None, None),
            size=(95, 35))
        self._result['card_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(387.5, self.height - 480),
            size_hint=(None, None),
            size=(95, 35))

        self._result['right_id_label'] = Label(text='Right id',
            pos=(545, self.height - 100),
            size_hint=(None, None),
            size=(175, 15))
        self._result['right_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(545, self.height - 150),
            size_hint=(None, None),
            size=(175, 35))
        self._result['right_label'] = Label(text='Name of right',
            pos=(545, self.height - 175),
            size_hint=(None, None),
            size=(175, 15))
        self._result['right_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(545, self.height - 225),
            size_hint=(None, None),
            size=(175, 35))
        self._result['right_was_added_label'] = Label(text='Date the right was added',
            pos=(532.5, self.height - 265),
            size_hint=(None, None),
            size=(200, 15))
        self._result['right_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(532.5, self.height - 315),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(637.5, self.height - 315),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_deleted_label'] = Label(text='Date the right was deleted',
            pos=(532.5, self.height - 355),
            size_hint=(None, None),
            size=(200, 15))
        self._result['right_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(532.5, self.height - 405),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(637.5, self.height - 405),
            size_hint=(None, None),
            size=(95, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}

        self._result['rule_id_label'] = Label(text='Id',
            pos=(50, self.height - 125),
            size_hint=(None, None),
            size=(175, 15))
        self._result['rule_id_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(50, self.height - 175),
            size_hint=(None, None),
            size=(175, 35))
        self._result['rule_was_added_label'] = Label(text='Date the rule was added',
            pos=(37.5, self.height - 225),
            size_hint=(None, None),
            size=(200, 15))
        self._result['rule_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(37.5, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['rule_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(142.5, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['rule_was_deleted_label'] = Label(text='Date the rule was deleted',
            pos=(37.5, self.height - 325),
            size_hint=(None, None),
            size=(200, 15))
        self._result['rule_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(37.5, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))
        self._result['rule_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(142.5, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))
        
        self._result['room_label'] = Label(text='Room',
            pos=(297.5, self.height - 125),
            size_hint=(None, None),
            size=(175, 15))
        room_dropdown = DropDown()
        # Запрос: список всех комнат из бд
        list_of_room = app.requsts_controller.get_table(table='rooms', start=-1)['data']
        list_of_room = [{'name': 'Room 1'}, {'name': 'Room 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_room) > 0:
            for room in list_of_room:
                button = btn.TipButton(text=room['name'],
                    size_hint=(None, None),
                    height=35,
                    width=175,
                    valign='center',
                    halign='center',
                    visible_symb=12)
                button.bind(on_press_event=lambda button:room_dropdown.select(button))
                room_dropdown.add_widget(button)
        self._result['room_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(297.5, self.height - 175),
            size_hint=(None, None),
            size=(175, 35))
        self._result['room_result'].bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(self._result['room_result'], 'text', x.text))
        room_dropdown.bind(on_select=lambda instance, x: x.on_leave())
        self._result['room_was_added_label'] = Label(text='Date the room was added',
            pos=(285, self.height - 225),
            size_hint=(None, None),
            size=(200, 15))
        self._result['room_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(285, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['room_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(390, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['room_was_deleted_label'] = Label(text='Date the room was deleted',
            pos=(285, self.height - 325),
            size_hint=(None, None),
            size=(200, 15))
        self._result['room_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(285, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))
        self._result['room_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(390, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))

        self._result['right_label'] = Label(text='Right',
            pos=(545, self.height - 125),
            size_hint=(None, None),
            size=(175, 15))
        right_dropdown = DropDown()
        # Запрос: список всех комнат из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1)['data']
        list_of_right = [{'name': 'Right 1'}, {'name': 'Right 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_right) > 0:
            for right in list_of_right:
                button = btn.TipButton(text=right['name'],
                    size_hint=(None, None),
                    height=35,
                    width=175,
                    valign='center',
                    halign='center',
                    visible_symb=12)
                button.bind(on_press_event=lambda button: right_dropdown.select(button))
                right_dropdown.add_widget(button)
        self._result['right_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(545, self.height - 175),
            size_hint=(None, None),
            size=(175, 35))
        self._result['right_result'].bind(on_release=right_dropdown.open)
        right_dropdown.bind(on_select=lambda instance, x: setattr(self._result['right_result'], 'text', x.text))
        right_dropdown.bind(on_select=lambda instance, x: x.on_leave())
        self._result['right_was_added_label'] = Label(text='Date the right was added',
            pos=(532.5, self.height - 225),
            size_hint=(None, None),
            size=(200, 15))
        self._result['right_was_added_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(532.5, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_added_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(637.5, self.height - 275),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_deleted_label'] = Label(text='Date the right was deleted',
            pos=(532.5, self.height - 325),
            size_hint=(None, None),
            size=(200, 15))
        self._result['right_was_deleted_date_result'] = TextInput(text='',
            hint_text='dd/mm/yy',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(532.5, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))
        self._result['right_was_deleted_time_result'] = TextInput(text='',
            hint_text='hh/mm/ss',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(637.5, self.height - 375),
            size_hint=(None, None),
            size=(95, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def confirm_dismiss(self, instance):
        res = {}
        if self._entity == 'cards':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        print(res)
        print('Confirm')
        self.dismiss()

class AddRecordWindow(Popup):
    _result = {}
    _entity = StringProperty()

    def __init__(self, **kwargs):
        super(AddRecordWindow, self).__init__(**kwargs)

    def open_win(self, entity):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self._entity = entity

        self.open()

    def on_open(self):
        self.add_menu()

    def add_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self.ids.main_area.add_widget(btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self))

        if self._entity == 'cards':
            self.menu_card()
        elif self._entity == 'rooms':
            self.menu_room()
        elif self._entity == 'rights':
            self.menu_right()
        elif self._entity == 'entities_view':
            self.menu_link()
        elif self._entity == 'access_rules_view':
            self.menu_rule()

    def menu_card(self):
        self._result = {}

        self._result['card_label'] = Label(text='Card number',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}

        self._result['room_name_label'] = Label(text='Room name',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['room_name_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}

        self._result['right_name_label'] = Label(text='Right name',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['right_name_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}

        self._result['card_label'] = Label(text='Card number',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(250, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(250, 35))
        
        self._result['sid_label'] = Label(text='sid',
            pos=(25, self.height - 225),
            size_hint=(None, None),
            size=(250, 15))
        self._result['sid_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 275),
            size_hint=(None, None),
            size=(250, 35))
        
        self._result['type_label'] = Label(text='Type',
            pos=(325, self.height - 125),
            size_hint=(None, None),
            size=(100, 15))
        type_dropdown = DropDown()
        choice_btn_1 = Button(text='User',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            size_hint_y=None,
            height=35)
        choice_btn_1.bind(on_release=lambda choice_btn_1: type_dropdown.select(choice_btn_1.text))
        type_dropdown.add_widget(choice_btn_1)
        choice_btn_2 = Button(text='Group',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            size_hint_y=None,
            height=35)
        choice_btn_2.bind(on_release=lambda choice_btn_2: type_dropdown.select(choice_btn_2.text))
        type_dropdown.add_widget(choice_btn_2)
        self._result['type_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            border=[10, 10, 10, 10],
            pos=(325, self.height - 175),
            size_hint=(None, None),
            size=(100, 35))
        self._result['type_result'].bind(on_release=type_dropdown.open)
        type_dropdown.bind(on_select=lambda instance, x: setattr(self._result['type_result'], 'text', x))

        self._result['right_label'] = Label(text='Right',
            pos=(450, self.height - 125),
            size_hint=(None, None),
            size=(100, 15))
        right_dropdown = DropDown()
        # Запрос: список всех прав из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1)['data']
        list_of_right = [{'name': 'Right 1'}, {'name': 'Right 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_right) > 0:
            for right in list_of_right:
                button = btn.TipButton(text=right['name'],
                    size_hint=(None, None),
                    height=35,
                    width=100,
                    valign='center',
                    halign='center',
                    visible_symb=7)
                button.bind(on_press_event=lambda button: right_dropdown.select(button))
                right_dropdown.add_widget(button)
        self._result['right_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(450, self.height - 175),
            size_hint=(None, None),
            size=(100, 35))
        self._result['right_result'].bind(on_release=right_dropdown.open)
        right_dropdown.bind(on_select=lambda instance, x: setattr(self._result['right_result'], 'text', x.text))
        right_dropdown.bind(on_select=lambda instance, x: x.on_leave())

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}

        self._result['room_label'] = Label(text='Room',
            pos=(60, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        room_dropdown = DropDown()
        # Запрос: список всех комнат из бд
        list_of_room = app.requsts_controller.get_table(table='rooms', start=-1)['data']
        list_of_room = [{'name': 'Room 1'}, {'name': 'Room 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_room) > 0:
            for room in list_of_room:
                button = btn.TipButton(text=room['name'],
                    size_hint=(None, None),
                    height=35,
                    width=200,
                    valign='center',
                    halign='center',
                    visible_symb=14)
                button.bind(on_press_event=lambda button: room_dropdown.select(button))
                room_dropdown.add_widget(button)
        self._result['room_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(60, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['room_result'].bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(self._result['room_result'], 'text', x.text))
        room_dropdown.bind(on_select=lambda instance, x: x.on_leave())

        self._result['right_label'] = Label(text='Right',
            pos=(325, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        right_dropdown = DropDown()
        # Запрос: список всех прав из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1)['data']
        list_of_right = [{'name': 'Right 1'}, {'name': 'Right 4aaaaaaaaaaaaaaaaaaaaaaaaa'}]
        if len(list_of_right) > 0:
            for right in list_of_right:
                button = btn.TipButton(text=right['name'],
                    size_hint=(None, None),
                    height=35,
                    width=200,
                    valign='center',
                    halign='center',
                    visible_symb=14)
                button.bind(on_press_event=lambda button: right_dropdown.select(button))
                right_dropdown.add_widget(button)
        self._result['right_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(325, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['right_result'].bind(on_release=right_dropdown.open)
        right_dropdown.bind(on_select=lambda instance, x: setattr(self._result['right_result'], 'text', x.text))
        right_dropdown.bind(on_select=lambda instance, x: x.on_leave())

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def confirm_dismiss(self, instance):
        res = {}
        if self._entity == 'cards':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        
        print('Confirm')
        self.dismiss()

class EditRecordWindow(Popup):
    _result = {}
    _entity = StringProperty()

    def __init__(self, **kwargs):
        super(EditRecordWindow, self).__init__(**kwargs)

    def open_win(self, entity):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self._entity = entity

        self.open()

    def on_open(self):
        self.edit_menu()

    def edit_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self.ids.main_area.add_widget(btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self))

        if self._entity == 'cards':
            self.menu_card()
        elif self._entity == 'rooms':
            self.menu_room()
        elif self._entity == 'rights':
            self.menu_right()
        elif self._entity == 'entities_view':
            self.menu_link()
        elif self._entity == 'access_rules_view':
            self.menu_rule()

    def menu_card(self):
        self._result = {}

        self._result['...'] = Label(text='Edit card',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}

        self._result['...'] = Label(text='Edit room',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}

        self._result['...'] = Label(text='Edit right',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}

        self._result['...'] = Label(text='Edit link',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}

        self._result['...'] = Label(text='Edit rule',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def confirm_dismiss(self, instance, type):
        res = {}
        if type == 'card':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        print(res)
        print('Confirm')
        self.dismiss()

class DeleteRecordWindow(Popup):
    _result = {}
    _entity = StringProperty()

    def __init__(self, **kwargs):
        super(DeleteRecordWindow, self).__init__(**kwargs)

    def open_win(self, entity):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self._entity = entity

        self.open()

    def on_open(self):
        self.delete_menu()

    def delete_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self.ids.main_area.add_widget(btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self))

        if self._entity == 'cards':
            self.menu_card()
        elif self._entity == 'rooms':
            self.menu_room()
        elif self._entity == 'rights':
            self.menu_right()
        elif self._entity == 'entities_view':
            self.menu_link()
        elif self._entity == 'access_rules_view':
            self.menu_rule()

    def menu_card(self):
        self._result = {}

        self._result['card_label'] = Label(text='Card id',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}

        self._result['room_label'] = Label(text='Room id',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['room_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}

        self._result['right_label'] = Label(text='Right id',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['right_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}

        self._result['link_label'] = Label(text='Link id',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['link_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}

        self._result['rule_label'] = Label(text='Rule id',
            pos=(110, self.height - 125),
            size_hint=(None, None),
            size=(350, 15))
        self._result['rule_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(110, self.height - 175),
            size_hint=(None, None),
            size=(350, 35))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(*args))

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def confirm_dismiss(self, instance):
        res = {}
        if self._entity == 'cards':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        print('Confirm')
        self.dismiss()

class CardsListWindow(Popup):
    close_button = None

    def __init__(self, **kwargs):
        super(CardsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_size(self, *args):
        if self.close_button:
            self.ids.table.remove_widget(self.close_button)
        self.close_button = btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self)
        self.ids.table.add_widget(self.close_button)

    def on_open(self):
        self.ids.cards_list_table.load_data(app.requsts_controller.get_table(table='cards', start=0))
        self._update()
    
    def _update(self):
        self.ids.cards_list_header._update()
        self.ids.cards_list_table._update()

class RoomsListWindow(Popup):
    close_button = None
    
    def __init__(self, **kwargs):
        super(RoomsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_size(self, *args):
        if self.close_button:
            self.ids.table.remove_widget(self.close_button)
        self.close_button = btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self)
        self.ids.table.add_widget(self.close_button)

    def on_open(self):
        self.ids.rooms_list_table.load_data(app.requsts_controller.get_table(table='rooms', start=0))
        self._update()
    
    def _update(self):
        self.ids.rooms_list_header._update()
        self.ids.rooms_list_table._update()

class RightsListWindow(Popup):
    close_button = None
    
    def __init__(self, **kwargs):
        super(RightsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_size(self, *args):
        if self.close_button:
            self.ids.table.remove_widget(self.close_button)
        self.close_button = btn.CloseButton(pos=(self.width - 60, self.height - 57.5),
            size_hint=(None, None),
            size=(25, 25),
            win=self)
        self.ids.table.add_widget(self.close_button)

    def on_open(self):
        self.ids.rights_list_table.load_data(app.requsts_controller.get_table(table='rights', start=0))
        self._update()
    
    def _update(self):
        self.ids.rights_list_header._update()
        self.ids.rights_list_table._update()
