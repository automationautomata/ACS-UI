import kivy
kivy.require('1.9.0')

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Rectangle, Line, Triangle

from kivy.properties import ObjectProperty, BooleanProperty, StringProperty, ListProperty, NumericProperty

global app


class HoverBehavior(object):
    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

class RootButton(Button, HoverBehavior):
    background_color = (0, 0, 0, 0)
    bg_normal_color = ListProperty([1, 0, 0, 1])
    bg_down_color = ListProperty([0, 1, 0, 1])
    bg_hover_color = ListProperty([0, 0, 1, 1])
    font_color = ListProperty([1, 1, 1, 1])
    check_collide = False
    bg_border = 0

    def __init__(self, **kwargs):
        super(RootButton, self).__init__(**kwargs)
        self.register_event_type('on_press_event')
        self._update()

    def on_touch_down(self, touch):
        if self.disabled:
            return
        if self.collide_point(*touch.pos):
            if 'button' in touch.profile:
                if touch.button == 'left':
                    self.check_collide = True
                    self._update(self.bg_down_color)
                    return
            self._update(self.bg_hover_color)

    def on_touch_up(self, touch):
        if self.disabled:
            return
        
        if self.check_collide:
            if self.collide_point(*touch.pos):
                self.dispatch('on_press_event')
                self._update(self.bg_hover_color)
                self.check_collide = False
                return
            self._update()
            self.check_collide = False

    def on_enter(self):
        if self.disabled:
            return
        self._update(self.bg_hover_color)

    def on_leave(self):
        if self.disabled:
            return
        self._update()

    def _update(self, color=None):
        if color is None:
            color = self.bg_normal_color
        self.canvas.before.clear()
        self.color = self.font_color
        
        self.pre_graphic_event()
        with self.canvas.before:
            Color(*color)
            Rectangle(pos=(self.x + self.bg_border, self.y + self.bg_border),
                size=(self.width - 2 * self.bg_border, self.height - 2 * self.bg_border))
        self.post_graphic_event()
    
    def on_press_event(self):
        pass
    
    def post_graphic_event(self):
        pass

    def pre_graphic_event(self):
        pass

class Tooltip(Label):
    def __init__(self, **kwargs):
        super(Tooltip, self).__init__(**kwargs)
        self.pos = (Window.mouse_pos[0] + 25, Window.mouse_pos[1] + 25)
        self.size_hint = (None, None)
        self.text_size = (300, None)
        self.size = (300, 100)
        self.valign = 'center'
        self.halign = 'center'
        self._update()

    def _update(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)
            Rectangle(size=self.size, pos=self.pos)

class TipButton(RootButton):
    tip_text = StringProperty('')
    def __init__(self, tip_text, **kwargs):
        super(TipButton, self).__init__(**kwargs)
        self.tip_text = tip_text

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

    def on_enter(self):
        if self.disabled:
            return
        self._update(self.bg_hover_color)
        self.tooltip = Tooltip(text=self.tip_text)
        Window.add_widget(self.tooltip)

    def on_leave(self):
        if self.disabled:
            return
        self._update()
        Window.remove_widget(self.tooltip)

class ShowDeletedRecordsCheckBox(FloatLayout):
    _table = StringProperty()
    _root = None
    def __init__(self, **kwargs):
        super(ShowDeletedRecordsCheckBox, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (210, 30)
        self.bind(_table=self._update)

    def on_pos(self, *args):
        if self._table:
            self._update()

    def _update(self, *args):
        self.clear_widgets()
        if self._table == 'entities_view' or self._table == 'access_rules_view':
            font_color = app.themes[app.current_theme]['Text']
        else:
            font_color = [1, 1, 1]
        checkbox = CheckBox(pos=self.pos,
            size_hint=(None, None),
            size=(30, 30),
            color=font_color,
            active=app.requsts_controller.get_sorting_rules(self._table)['deleted_record'])
        checkbox.bind(active=self.on_checkbox_active)
        label = Label(text='Show deleted record',
            pos=(self.x + 35, self.y),
            size_hint=(None, None),
            size=(170, 28),
            color=font_color)
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

class ThemeButton(RootButton):
    def __init__(self, **kwargs):
        super(ThemeButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def switch_theme(self, _root):
        app.current_theme = (app.current_theme + 1) % len(app.themes)
        _root._update()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class DomainButton(RootButton):
    def __init__(self, **kwargs):
        super(DomainButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

    def DomainWindow(self):
        pass

class FindButton(RootButton):
    def __init__(self, **kwargs):
        super(FindButton, self).__init__(**kwargs)
        
    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class AddRecordButton(RootButton):
    def __init__(self, **kwargs):
        super(AddRecordButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class EditRecordButton(RootButton):
    def __init__(self, **kwargs):
        super(EditRecordButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class DeleteRecordButton(RootButton):
    def __init__(self, **kwargs):
        super(DeleteRecordButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class CardsListButton(RootButton):
    def __init__(self, **kwargs):
        super(CardsListButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class RoomsListButton(RootButton):
    def __init__(self, **kwargs):
        super(RoomsListButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class RightsListButton(RootButton):
    def __init__(self, **kwargs):
        super(RightsListButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][2]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class ExplorerButton(RootButton):
    def __init__(self, **kwargs):
        super(ExplorerButton, self).__init__(**kwargs)

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self, *args):
        self.bg_normal_color = app.themes[app.current_theme]['Base'][2]
        self.bg_down_color = app.themes[app.current_theme]['Base'][1]
        self.bg_hover_color = app.themes[app.current_theme]['Base'][0]
        self.font_color = app.themes[app.current_theme]['Text']
        self._update()

class CloseButton(RootButton):
    window = None
    check_collide = False

    def __init__(self, win, **kwargs):
        super(CloseButton, self).__init__(**kwargs)
        self.window = win

    def on_kv_post(self, widget):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = [.6, .6, .6, 1]
        self.bg_down_color = [.6, .1, .1, 1]
        self.bg_hover_color = [.75, .05, .05, 1]
        self._update()

    def on_press_event(self):
        self.window.dismiss()

    def post_graphic_event(self):
        with self.canvas.before:
            Color(0, 0, 0, .7)
            Line(points=(self.x + 5, self.y + 5, self.right - 5, self.top - 5), width=2)
            Line(points=(self.right - 5, self.y + 5, self.x + 5, self.top - 5), width=2)

class TitleButton(RootButton):
    root = None

    def __init__(self, column_key, parent, **kwargs):
        self.root = parent
        super(TitleButton, self).__init__(**kwargs)

    def on_size(self, *args):
        self._update_theme()

    def _update_theme(self):
        self.bg_normal_color = app.themes[app.current_theme]['Additionally'][0]
        self.bg_down_color = app.themes[app.current_theme]['Additionally'][3]
        self.bg_hover_color = app.themes[app.current_theme]['Additionally'][1]
        self.bg_border = 1
        self._update()

    def on_press_event(self):
        app.requsts_controller.switch_sorting_rules(table=self.root._table,
            column=self.root._data_keys[self.root._data_titles.index(self.text)])

    def pre_graphic_event(self):
        with self.canvas.before:
            Color(*app.themes[app.current_theme]['Base'][0])
            Rectangle(pos=self.pos, size=self.size)

    def post_graphic_event(self):
        with self.canvas.before:
            if self.root._data_keys[self.root._data_titles.index(self.text)] == app.requsts_controller.get_sorting_rules(self.root._table)['column']:
                if app.requsts_controller.get_sorting_rules(self.root._table)['rule'] == 'A-Z':
                    Color(*app.themes[app.current_theme]['Text'])
                    Line(points=[self.x + self.width - 20, 14, self.x + self.width - 20, 32], width=1.3, cap='round')
                    Triangle(points=[self.x + self.width - 25, 32, self.x + self.width - 15, 32, self.x + self.width - 20, 37])
                elif app.requsts_controller.get_sorting_rules(self.root._table)['rule'] == 'Z-A':
                    Color(*app.themes[app.current_theme]['Text'])
                    Line(points=[self.x + self.width - 20, 17, self.x + self.width - 20, 35], width=1.3, cap='round')
                    Triangle(points=[self.x + self.width - 25, 17, self.x + self.width - 15, 17, self.x + self.width - 20, 12])
                else:
                    pass
