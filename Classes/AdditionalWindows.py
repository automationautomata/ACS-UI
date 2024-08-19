import kivy
kivy.require('1.9.0')

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle

from kivy.properties import StringProperty, ListProperty, NumericProperty

global app


class Tooltip(Label):
    def __init__(self, **kwargs):
        super(Tooltip, self).__init__(**kwargs)

    def on_size(self, *args):
        self.canvas.before.clear()
        self.pos = (1137.5, 600 - self.texture_size[1])
        self.size_hint = (None, None)
        self.size = self.texture_size
        self.valign = 'top'
        self.halign = 'left'
        with self.canvas.before:
            Color(0, 0, 0, 1)
            Rectangle(size=self.size, pos=self.pos)

class TipButton(Button):
    tooltip = None

    def __init__(self, tip_text, **kwargs):
        self.tooltip = Tooltip(text=tip_text)
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(TipButton, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        Clock.unschedule(self.display_tooltip)
        self.close_tooltip()
        if self.collide_point(*self.to_widget(*pos)):
            Clock.schedule_once(self.display_tooltip, 1)

    def close_tooltip(self, *args):
        Window.remove_widget(self.tooltip)

    def display_tooltip(self, *args):
        Window.add_widget(self.tooltip)


class DomainWindow(Popup):
    def __init__(self, **kwargs):
        super(DomainWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

class SortingWindow(Popup):
    def __init__(self, **kwargs):
        super(SortingWindow, self).__init__(**kwargs)

    def open_win(self, entity):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self._entity = entity

        self.open()

    def on_open(self):
        self.sorting_menu()

    def sorting_menu(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        if self._entity == 'card':
            self.sorting_card()
        elif self._entity == 'room':
            self.sorting_room()
        elif self._entity == 'right':
            self.sorting_right()
        elif self._entity == 'link':
            self.sorting_link()
        elif self._entity == 'rule':
            self.sorting_rule()
        elif self._entity == 'logs':
            self.sorting_logs()

    def sorting_card(self):
        pass

    def sorting_room(self):
        pass

    def sorting_right(self):
        pass

    def sorting_link(self):
        pass

    def sorting_rule(self):
        pass

    def sorting_logs(self):
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

        if self._entity == 'card':
            self.find_card()
        elif self._entity == 'room':
            self.find_room()
        elif self._entity == 'right':
            self.find_right()
        elif self._entity == 'link':
            self.find_link()
        elif self._entity == 'rule':
            self.find_rule()
        elif self._entity == 'logs':
            self.find_logs()

    def find_card(self):
        pass

    def find_room(self):
        pass

    def find_right(self):
        pass

    def find_link(self):
        pass

    def find_rule(self):
        pass

    def find_logs(self):
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

        if self._entity == 'card':
            self.add_card()
        elif self._entity == 'room':
            self.add_room()
        elif self._entity == 'right':
            self.add_right()
        elif self._entity == 'link':
            self.add_link()
        elif self._entity == 'rule':
            self.add_rule()

    def add_card(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['card_label'] = Label(text='Card number',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(445, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(445, 35))

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

    def add_room(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['room_name_label'] = Label(text='Room name',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(445, 15))
        self._result['room_name_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(445, 35))

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

    def add_right(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['right_name_label'] = Label(text='Right name',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(445, 15))
        self._result['right_name_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(445, 35))

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

    def add_link(self):
        self._result = {}
        self.ids.main_area.clear_widgets()

        self._result['card_label'] = Label(text='Card number',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        self._result['card_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['sid_label'] = Label(text='sid',
            pos=(25, self.height - 225),
            size_hint=(None, None),
            size=(200, 15))
        self._result['sid_result'] = TextInput(text='',
            cursor_color=app.themes[app.current_theme]['Additionally'][2],
            multiline=False,
            pos=(25, self.height - 275),
            size_hint=(None, None),
            size=(200, 35))
        self._result['type_label'] = Label(text='Type',
            pos=(250, self.height - 125),
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
            pos=(250, self.height - 175),
            size_hint=(None, None),
            size=(100, 35))
        self._result['type_result'].bind(on_release=type_dropdown.open)
        type_dropdown.bind(on_select=lambda instance, x: setattr(self._result['type_result'], 'text', x))
        self._result['right_label'] = Label(text='Right',
            pos=(375, self.height - 125),
            size_hint=(None, None),
            size=(100, 15))
        right_dropdown = DropDown()

        # Запрос: список всех прав из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1, sorting_rules={})['data']

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
            pos=(375, self.height - 175),
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

    def add_rule(self):
        self._result = {}
        self.ids.main_area.clear_widgets()


        self._result['room_label'] = Label(text='Room',
            pos=(25, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        room_dropdown = DropDown()


        # Запрос: список всех комнат из бд
        list_of_room = app.requsts_controller.get_table(table='room', start=-1, sorting_rules={})['data']

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
            pos=(25, self.height - 175),
            size_hint=(None, None),
            size=(200, 35))
        self._result['room_result'].bind(on_release=room_dropdown.open)
        room_dropdown.bind(on_select=lambda instance, x: setattr(self._result['room_result'], 'text', x))


        self._result['right_label'] = Label(text='Right',
            pos=(270, self.height - 125),
            size_hint=(None, None),
            size=(200, 15))
        right_dropdown = DropDown()
        # Запрос: список всех прав из бд
        list_of_right = app.requsts_controller.get_table(table='rights', start=-1, sorting_rules={})['data']

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
            pos=(270, self.height - 175),
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
        print(res)
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

        if self._entity == 'card':
            self.edit_card()
        elif self._entity == 'room':
            self.edit_room()
        elif self._entity == 'right':
            self.edit_right()
        elif self._entity == 'link':
            self.edit_link()
        elif self._entity == 'rule':
            self.edit_rule()

    def edit_card(self):
        pass

    def edit_room(self):
        pass

    def edit_right(self):
        pass

    def edit_link(self):
        pass

    def edit_rule(self):
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

class DeleteRecordWindow(Popup):
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

        if self._entity == 'card':
            self.delete_card()
        elif self._entity == 'room':
            self.delete_room()
        elif self._entity == 'right':
            self.delete_right()
        elif self._entity == 'link':
            self.delete_link()
        elif self._entity == 'rule':
            self.delete_rule()

    def delete_card(self):
        pass

    def delete_room(self):
        pass

    def delete_right(self):
        pass

    def delete_link(self):
        pass

    def delete_rule(self):
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

class CardsListWindow(Popup):
    def __init__(self, **kwargs):
        super(CardsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.cards_list_table.load_data(app.requsts_controller.get_table(table='cards', start=0, sorting_rules={}))
        self.ids.cards_list_header.load_data()
       
class RoomsListWindow(Popup):
    def __init__(self, **kwargs):
        super(RoomsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.rooms_list_table.load_data(app.requsts_controller.get_table(table='rooms', start=0, sorting_rules={}))
        self.ids.rooms_list_header.load_data()

class RightsListWindow(Popup):
    def __init__(self, **kwargs):
        super(RightsListWindow, self).__init__(**kwargs)

    def open_win(self):
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.separator_color = app.themes[app.current_theme]['Base'][0]
        self.open()

    def on_open(self):
        self.ids.rights_list_table.load_data(app.requsts_controller.get_table(table='rights', start=0, sorting_rules={}))
        self.ids.rights_list_header.load_data()
