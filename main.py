import kivy
kivy.require('1.9.0')
from kivy.config import Config
import os
Config.read(os.path.split(os.path.realpath(__file__))[0] + '\\' + 'config.ini')

import Classes.skud_api as api
import Classes.Buttons as btn
import Classes.Table as tbl
import Classes.Screens  as scr
import Classes.AdditionalWindows as addit_win

from kivy.app import App
from kivy.lang import Builder

Builder.load_file('MyMain.kv')
api_args = "http://localhost:9092", 1
class TestApp(App):
    def __init__(self, **kwargs):
        App.__init__(self)
        self.requsts_controller = api.SkudApiRequests(url=api_args[0], id=api_args[1])
        self.current_theme = 0
        self.themes = [
                {
                    'Base': [[0, .01, .2], [.07, .07, .4], [.2, .2, .5]],
                    'Additionally': [[.01, .3, .3], [.05, .4, .3], [.2, .35, .3], [.007, .25, .25]],
                    'Accent': [[.9, .05, .3], [.9, .3, .5], [.65, .05, .2]],
                    'Text': [1, 1, 1]
                },
                {
                    'Base': [[.85, .9, 1], [.75, .8, .9], [.75, .75, .9]],
                    'Additionally': [[.85, .6, .8], [.75, .5, .7], [.85, .7, .85], [.8, .55, .75]],
                    'Accent': [[.9, .8, .05], [.8, .7, .01], [.9, .8, .3]],
                    'Text': [0, 0, 0]
                },
                {
                    'Base': [[.15, .1, 0], [.2, .12, 0], [.3, .15, 0]],
                    'Additionally': [[.35, .25, .05], [.4, .3, .15], [.5, .4, .3], [.3, .2, .01]],
                    'Accent': [[.05, .04, .03], [.25, .25, .25], [.97, .96, .95]],
                    'Text': [1, 1, 1]
                },
                {
                    'Base': [[.8, .8, .8], [.85, .95, .85], [.65, .65, .65]],
                    'Additionally': [[.1, .45, .1], [.15, .4, .15], [.35, .55, .35], [.05, .4, .05]],
                    'Accent': [[0, 0, .6], [.1, .1, .7], [.25, .25, .8]],
                    'Text': [0, 0, 0]
                }]

    def build(self):
        btn.app = self
        tbl.app = self
        scr.app = self
        addit_win.app = self
        ms = scr.MainScreen()

        return ms

if __name__ == '__main__':
    TestApp().run()