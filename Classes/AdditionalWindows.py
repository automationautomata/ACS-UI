import kivy
import Classes.Buttons
kivy.require('1.9.0')

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

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
        elif self._entity == 'logs':
            self.menu_logs()

    def menu_card(self):
        pass

    def menu_room(self):
        pass

    def menu_right(self):
        pass

    def menu_link(self):
        pass

    def menu_rule(self):
        pass

    def menu_logs(self):
        pass

    def confirm_dismiss(self, instance, type):
        res = {}
        if type == 'card':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        print(res)
        print('Confirm')
        self.dismiss()

    def cancel_dismiss(self, instance):
        print('Cancel')
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
        self.ids.main_area.clear_widgets()

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
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(type='card', *args))
        self._result['cancel_button'] = Button(text='Cancel',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 240, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['cancel_button'].bind(on_release=self.cancel_dismiss)

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

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
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(type='room', *args))
        self._result['cancel_button'] = Button(text='Cancel',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 240, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['cancel_button'].bind(on_release=self.cancel_dismiss)

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

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
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(type='right', *args))
        self._result['cancel_button'] = Button(text='Cancel',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 240, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['cancel_button'].bind(on_release=self.cancel_dismiss)

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

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

        if len(list_of_right) > 0:
            for right in list_of_right:
                btn = TipButton(text=right['name'],
                    tip_text=right['name'],
                    background_normal='',
                    background_color=app.themes[app.current_theme]['Additionally'][0],
                    size_hint_y=None,
                    height=35,
                    text_size=(100, 35),
                    valign='center',
                    halign='center',
                    shorten=True,
                    shorten_from='right',
                    split_str='')
                btn.bind(on_release=lambda btn: right_dropdown.select(btn.text))
                right_dropdown.add_widget(btn)
        self._result['right_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(450, self.height - 175),
            size_hint=(None, None),
            size=(100, 35))
        self._result['right_result'].bind(on_release=right_dropdown.open)
        right_dropdown.bind(on_select=lambda instance, x: setattr(self._result['right_result'], 'text', x))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(type='link', *args))
        self._result['cancel_button'] = Button(text='Cancel',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 240, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['cancel_button'].bind(on_release=self.cancel_dismiss)

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}
        self.ids.main_area.clear_widgets()


        self._result['room_label'] = Label(text='Room',
            pos=(60, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        room_dropdown = DropDown()


        # Запрос: список всех комнат из бд
        list_of_room = app.requsts_controller.get_table(table='room', start=-1)['data']

        if len(list_of_room) > 0:
            for room in list_of_room:
                btn = TipButton(text=room['name'],
                    tip_text=room['name'],
                    background_normal='',
                    background_color=app.themes[app.current_theme]['Additionally'][0],
                    size_hint_y=None,
                    height=35,
                    text_size=(100, 35),
                    valign='center',
                    halign='center',
                    shorten=True,
                    shorten_from='right',
                    split_str='')
                btn.bind(on_release=lambda btn: room_dropdown.select(btn.text))
                room_dropdown.add_widget(btn)
        self._result['room_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(60, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['room_result'].bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(self._result['room_result'], 'text', x))


        self._result['right_label'] = Label(text='Right',
            pos=(315, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        right_dropdown = DropDown()
        # Запрос: список всех прав из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1)['data']

        if len(list_of_right) > 0:
            for right in list_of_right:
                btn = TipButton(text=right['name'],
                    tip_text=right['name'],
                    background_normal='',
                    background_color=app.themes[app.current_theme]['Additionally'][0],
                    size_hint_y=None,
                    height=35,
                    text_size=(100, 35),
                    valign='center',
                    halign='center',
                    shorten=True,
                    shorten_from='right',
                    split_str='')
                btn.bind(on_release=lambda btn: right_dropdown.select(btn.text))
                right_dropdown.add_widget(btn)
        self._result['right_result'] = Button(text='Choose...',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(315, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['right_result'].bind(on_release=right_dropdown.open)
        right_dropdown.bind(on_select=lambda instance, x: setattr(self._result['right_result'], 'text', x))

        self._result['confirm_button'] = Button(text='Confirm',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 130, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['confirm_button'].bind(on_release=lambda *args: self.confirm_dismiss(type='right', *args))
        self._result['cancel_button'] = Button(text='Cancel',
            background_normal='',
            background_color=app.themes[app.current_theme]['Additionally'][0],
            pos=(self.width - 240, 0),
            size_hint=(None, None),
            size=(100, 35))
        self._result['cancel_button'].bind(on_release=self.cancel_dismiss)

        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def confirm_dismiss(self, instance, type):
        res = {}
        if type == 'card':
            # Запрос: проверка существования карты в бд
            res['number'] = self._result['card_result'].text
        
        print('Confirm')
        self.dismiss()

    def cancel_dismiss(self, instance):
        print('Cancel')
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
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Edit card',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Edit room',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Edit right',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Edit link',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

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

    def cancel_dismiss(self, instance):
        print('Cancel')
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
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Delete card',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_room(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Delete room',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_right(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Delete right',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_link(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Delete link',
            pos=(110, self.height - 200),
            size_hint=(None, None),
            size=(350, 15))
        
        for el in self._result.values():
            self.ids.main_area.add_widget(el)

    def menu_rule(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['...'] = Label(text='Delete rule',
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

    def cancel_dismiss(self, instance):
        print('Cancel')
        self.dismiss()

class CardsListWindow(Popup):
    def __init__(self, **kwargs):
        super(CardsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.cards_list_table.load_data(app.requsts_controller.get_table(table='cards', start=0))
        self._update()
    
    def _update(self):
        self.ids.cards_list_header._update()
        self.ids.cards_list_table._update()

class RoomsListWindow(Popup):
    def __init__(self, **kwargs):
        super(RoomsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.rooms_list_table.load_data(app.requsts_controller.get_table(table='rooms', start=0))
        self._update()
    
    def _update(self):
        self.ids.rooms_list_header._update()
        self.ids.rooms_list_table._update()

class RightsListWindow(Popup):
    def __init__(self, **kwargs):
        super(RightsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.rights_list_table.load_data(app.requsts_controller.get_table(table='rights', start=0))
        self._update()
    
    def _update(self):
        self.ids.rights_list_header._update()
        self.ids.rights_list_table._update()
