import kivy
kivy.require('1.9.0')

from kivy.core.window import Window

from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from kivy.graphics import BorderImage, Color, Line, Rectangle

global app

entities_db = [['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'] for _ in range(30)]
rules_db = [['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'] for _ in range(5)]

test = {'data': [{'card': '15',
                'isSabotagedCard': '0',
                'cardAddDate': '2024-08-08 20:29:38',
                'cardDelDate': None,
                'right': 1,
                'rightName': 'admin',
                'rightAddDate': '2024-08-08 20:29:38',
                'rightDelDate': None,
                'sid': 5,
                'type': '0',
                'entityAddDate': '2024-08-08 20:29:38',
                'entityDelDate': None}],
        'error': ''}

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.ids.entities_table.load_data(app.requsts_controller.get_table(table='entities_view', start=0))
        self.ids.access_rules_table.load_data(app.requsts_controller.get_table(table='access_rules_view', start=0))
        self._update()

    def _update(self):
        Window.clearcolor = app.themes[app.current_theme]['Base'][0]
        self.ids.entities_deleted_records._update()
        self.ids.access_rules_deleted_records._update()
        self.ids.theme_button._update()
        self.ids.domain_button._update()
        self.ids.add_record_button._update()
        self.ids.edit_record_button._update()
        self.ids.delete_record_button._update()
        self.ids.find_button._update()
        self.ids.cards_list_button._update()
        self.ids.rooms_list_button._update()
        self.ids.rights_list_button._update()
        self.ids.go_entites_screen._update()
        self.ids.go_access_rules_screen._update()
        self.ids.go_logs_screen._update()
        self.ids.footer._update()
        self.ids.entities_header._update()
        self.ids.entities_table._update()
        self.ids.access_rules_header._update()
        self.ids.access_rules_table._update()

class EntitiesScreen(Screen):
    pass

class RulesScreen(Screen):
    pass

class LogsScreen(Screen):
    pass


class Footer(Widget):
    def on_size(self, *args):
        self._update()

    def _update(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*app.themes[app.current_theme]['Additionally'][0])
            Rectangle(pos=self.pos, size=self.size)
