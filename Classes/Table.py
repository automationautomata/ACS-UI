import kivy
kivy.require('1.9.0')

from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Line, Triangle

from kivy.properties import StringProperty, ListProperty, NumericProperty

global app


class MyLabelHeader(Label):
    def __init__(self, column_key, **kwargs):
        super(MyLabelHeader, self).__init__(**kwargs)

    def on_size(self, *args):
        self._update(app.themes[app.current_theme]['Additionally'][0])

    def on_touch_down(self, touch):
        table_header = self.parent.parent
        if self.collide_point(*touch.pos):
            self._update(app.themes[app.current_theme]['Additionally'][3])
            app.requsts_controller.switch_sorting_rules(table=table_header._table,
                column=table_header._data_keys[table_header._data_titles.index(self.text)])

    def on_touch_up(self, touch):
        self._update(app.themes[app.current_theme]['Additionally'][0])

    def _update(self, back):
        table_header = self.parent.parent
        self.canvas.before.clear()
        self.color = app.themes[app.current_theme]['Text']

        with self.canvas.before:
            Color(*app.themes[app.current_theme]['Base'][0])
            Rectangle(pos=self.pos, size=self.size)
            Color(*back)
            Rectangle(pos=(self.x + 1, self.y + 1), size=(self.width - 2, self.height - 2))

            if table_header._data_keys[table_header._data_titles.index(self.text)] == app.requsts_controller.get_sorting_rules(table_header._table)['column']:
                if app.requsts_controller.get_sorting_rules(table_header._table)['rule'] == 'A-Z':
                    Color(*app.themes[app.current_theme]['Text'])
                    Line(points=[self.x + self.width - 20, 14, self.x + self.width - 20, 32], width=1.3, cap='round')
                    Triangle(points=[self.x + self.width - 25, 32, self.x + self.width - 15, 32, self.x + self.width - 20, 37])
                elif app.requsts_controller.get_sorting_rules(table_header._table)['rule'] == 'Z-A':
                    Color(*app.themes[app.current_theme]['Text'])
                    Line(points=[self.x + self.width - 20, 17, self.x + self.width - 20, 35], width=1.3, cap='round')
                    Triangle(points=[self.x + self.width - 25, 17, self.x + self.width - 15, 17, self.x + self.width - 20, 12])
                else:
                    pass

class MyLabelTable(Label):
    def __init__(self, **kwargs):
        super(MyLabelTable, self).__init__(**kwargs)

    def on_size(self, *args):
        self.parent_win = self.parent.parent
        self.canvas.before.clear()
        self.color = app.themes[app.current_theme]['Text']
        with self.canvas.before:
            Color(*app.themes[app.current_theme]['Base'][0])
            Rectangle(pos=self.pos, size=self.size)
            Color(*app.themes[app.current_theme]['Additionally'][2])
            Rectangle(pos=(self.x + 1, self.y + 1), size=(self.width - 2, self.height - 2))

class TableHeader(ScrollView):
    _grid = None
    _columns_width = ListProperty()
    _data_titles = ListProperty()
    _data_keys = ListProperty()
    _table = StringProperty()
    _root = None

    def __init__(self, **kwargs):
        super(TableHeader, self).__init__(**kwargs)
        self.bar_width = 0
        self.do_scroll_x = False
        self.do_scroll_y = False

    def _update(self, *args):
        self._grid.clear_widgets()
        for col in range(self._columns):
            label = MyLabelHeader(text=self._data_titles[col], column_key=self._data_keys[col])
            self._grid.add_widget(label)

    def _update_table_data(self):
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

    def scrolling(self, dist):
        if dist == 0:
            self.scroll_x = 0
        else:
            self.scroll_x = dist[0] / (1 - dist[1])

class TableContent(ScrollView):
    _grid = None
    _header = None
    _rows = NumericProperty()
    _columns_width = ListProperty()
    table_data = ListProperty()

    def __init__(self, **kwargs):
        super(TableContent, self).__init__(**kwargs)
        self.bar_width = 10
        self.scroll_type = ['bars'] # Перемещение с помощью ползунков
        self.always_overscroll = False
        self.smooth_scroll_end = 10
        self.do_scroll_x = True
        self.do_scroll_y = True

        self.bind(hbar=self.scroll_content)

    def load_data(self, test):
        if test['error']:
            raise NameError(test['error'])

        data = test['data']
        for record in range(len(data)):
            row = []
            for col in self._header._data_keys:
                if data[record][col] is not None and str(data[record][col]):
                    row.append(str(data[record][col]))
                else:
                    row.append('-')
            self.table_data.append(row)

        for empty in range(25 - len(self.table_data)):
            self.table_data.append(' ' * len(self._header._data_keys))

        self._update()

    def _update(self):
        self._grid.clear_widgets()
        for row in range(self._rows):
            for col in range(self._columns):
                label = MyLabelTable(text=self.table_data[row][col])
                self._grid.add_widget(label)

    def scroll_content(self, instance, value):
        self._header.scrolling(value)
