import kivy
kivy.require('1.9.0')

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
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

class ShowDeletedRecordsCheckBox(FloatLayout):
    _table = StringProperty()
    _root = None
    def __init__(self, **kwargs):
        super(ShowDeletedRecordsCheckBox, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (210, 30)
        self.bind(_table=self._update)

    def _update(self, *args):
        self.clear_widgets()

        checkbox = CheckBox(pos=self.pos,
            size_hint=(None, None),
            size=(30, 30),
            color=app.themes[app.current_theme]['Text'],
            active=app.requsts_controller.get_sorting_rules(self._table)['deleted_record'])
        checkbox.bind(active=self.on_checkbox_active)
        label = Label(text='Show deleted record',
            pos=(self.x + 35, self.y),
            size_hint=(None, None),
            size=(170, 28),
            color=app.themes[app.current_theme]['Text'])
        self.add_widget(checkbox)
        self.add_widget(label)

    def on_checkbox_active(self, instance, state):
        app.requsts_controller.switch_sorting_rules(table=self._table)

        if self._table == 'entities_view':
            self._root.ids.entities_table.load_data(app.requsts_controller.get_table(table='entities_view', start=0))
        elif self._table == 'access_rules_view':
            self._root.ids.access_rules_table.load_data(app.requsts_controller.get_table(table='access_rules_view', start=0))
        elif self._table == 'cards':
            self._root.ids.cards_list_table.load_data(app.requsts_controller.get_table(table='cards', start=0))
        elif self._table == 'rooms':
            self._root.ids.rooms_list_table.load_data(app.requsts_controller.get_table(table='rooms', start=0))
        elif self._table == 'rights':
            self._root.ids.rights_list_table.load_data(app.requsts_controller.get_table(table='rights', start=0))

class ThemeButton(Button):
    def __init__(self, **kwargs):
        super(ThemeButton, self).__init__(**kwargs)

    def switch_theme(self, _root):
        app.current_theme = (app.current_theme + 1) % len(app.themes)
        _root._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]

class DomainButton(Button):
    def __init__(self, **kwargs):
        super(DomainButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]

    def DomainWindow(self):
        pass

class FindButton(Button):
    def __init__(self, **kwargs):
        super(FindButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]

class AddRecordButton(Button):
    def __init__(self, **kwargs):
        super(AddRecordButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.disabled_background_color = app.themes[app.current_theme]['Additionally'][2]

class EditRecordButton(Button):
    def __init__(self, **kwargs):
        super(EditRecordButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]

class DeleteRecordButton(Button):
    def __init__(self, **kwargs):
        super(DeleteRecordButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]

class CardsListButton(Button):
    def __init__(self, **kwargs):
        super(CardsListButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.disabled_background_color = app.themes[app.current_theme]['Additionally'][2]

class RoomsListButton(Button):
    def __init__(self, **kwargs):
        super(RoomsListButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.disabled_background_color = app.themes[app.current_theme]['Additionally'][2]

class RightsListButton(Button):
    def __init__(self, **kwargs):
        super(RightsListButton, self).__init__(**kwargs)
        self._update()

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Additionally'][2]
        self.disabled_background_color = app.themes[app.current_theme]['Additionally'][2]

class ExplorerButton(Button):
    def __init__(self, **kwargs):
        super(ExplorerButton, self).__init__(**kwargs)

    def _update(self, *args):
        self.color = app.themes[app.current_theme]['Text']
        self.background_color = app.themes[app.current_theme]['Base'][2]
