from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.config import ConfigParser, Config
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
from kivy.core.window import Window
import os
import ast
import time
from money_data import CoinsData
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from controls.control_menu import ControlMenu


# Константы стартового экрана
CONST_COINS_IMG = os.path.join(os.getcwd(), 'coins_interface', 'coins.jpg')  # Стопка монет на стартовой
CONST_PAPER_IMG = os.path.join(os.getcwd(), 'coins_interface', 'paper.jpg')  # Стопка монет на стартовой

# Констынты коллекции монет
# CONST_10R_PATH = os.path.join(os.getcwd(), 'coins_interface', 'ten_rubles')
CONST_CURR_PATH = os.getcwd()


class StartScreen(Screen):
    """Стартовый экран. Выбор между просмотром коллекции монет и коллекции банкнот"""

    def __init__(self, **kw):
        super(StartScreen, self).__init__(**kw)

        # Стартовый экран состоит из одного виджета - BoxLayout
        top_text = Label(text="ВЫБЕРИТЕ КОЛЛЕКЦИЮ", font_size=24)
        top = BoxLayout(orientation='vertical', size_hint=(1, .2))
        top.add_widget(top_text)

        grid = BoxLayout(orientation='vertical', spacing=30)
        grid.add_widget(Button(background_normal=CONST_COINS_IMG, size_hint=(.65, 1),
                               pos_hint={'center_x': .5, 'center_y': .5},
                               on_press=lambda x: set_screen('coins_collection')))

        grid.add_widget(Button(background_normal=CONST_PAPER_IMG, size_hint=(.7, 1),
                               pos_hint={'center_x': .5, 'center_y': .5},
                               on_press=lambda x: set_screen('paper_collection')))
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(top)
        self.layout.add_widget(grid)
        self.add_widget(self.layout)


class CoinsCollection(Screen):
    def __init__(self, **kw):
        super(CoinsCollection, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=2, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        coin_db = CoinsData()
        all_coins = coin_db.get_coins_info()
        for coin in all_coins:
            coin_box = BoxLayout(orientation='vertical', size_hint_y=None)
            coin_img = Button(background_normal=os.path.join(CONST_CURR_PATH, coin['img_path']), size_hint=(0.6, None))
            coin_info = Label(
                text='Серия: {}\nГод: {}\nСтрана: {}'.format(coin['seria'], coin['year'], coin['country']),
                font_size=10)
            coin_box.add_widget(coin_img)
            coin_box.add_widget(coin_info)
            self.layout.add_widget(coin_box)

        # Кнопка возврата на главное меню
        # back_button = Button(text='ДОМОЙ',
        #                      on_press=lambda x: set_screen('start_menu'),
        #                      size_hint_y=None, height=40)
        #
        # add_button = Button(text=' + ', on_press=lambda x: set_screen('add_coin'),
        #                     size_hint_y=None, height=40)

        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), pos_hint={'top': 0.93})
        scroll.add_widget(self.layout)
        self.add_widget(scroll)
        # menu = BoxLayout(orientation='
        menu = ControlMenu(home_action=lambda x: set_screen('start_menu'),
                           add_action=lambda x: set_screen('add_coin'))
        self.add_widget(menu)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана
        self.layout.clear_widgets()  # очищаем список


class PaperCollection(Screen):
    def __init__(self, **kw):
        super(PaperCollection, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад к выбору коллекции',
                             on_press=lambda x: set_screen('start_menu'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список


class AddCoin(Screen):
    """Класс для добавления новых монет"""

    def __init__(self, **kw):
        super(AddCoin, self).__init__(**kw)

    def on_enter(self):

        self.layout = BoxLayout(orientation='vertical')
        top_text = Label(text="Для добавления монеты\n         заполните поля", font_size=16)
        back_button = Button(text='< Назад к коллекции монет',
                             on_press=lambda x: set_screen('coins_collection'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(top_text)
        self.layout.add_widget(back_button)
        self.add_widget(self.layout)
        menu = ControlMenu(home_action=lambda x: set_screen('coins_collection'),
                           add_action=lambda x: set_screen('add_coin'))
        self.add_widget(menu)

#
#
# class AddFood(Screen):
#
#     def buttonClicked(self, btn1):
#         if not self.txt1.text:
#             return
#         self.app = App.get_running_app()
#         self.app.user_data = ast.literal_eval(
#             self.app.config.get('General', 'user_data'))
#         self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())
#
#         self.app.config.set('General', 'user_data', self.app.user_data)
#         self.app.config.write()
#
#         text = "Последнее добавленное блюдо:  " + self.txt1.text
#         self.result.text = text
#         self.txt1.text = ''
#
#     def __init__(self, **kw):
#         super(AddFood, self).__init__(**kw)
#         box = BoxLayout(orientation='vertical')
#         back_button = Button(text='< Назад в главное меню', on_press=lambda x:
#                              set_screen('menu'), size_hint_y=None, height=dp(40))
#         box.add_widget(back_button)
#         self.txt1 = TextInput(text='', multiline=False, height=dp(40),
#                               size_hint_y=None, hint_text="Название блюда")
#         box.add_widget(self.txt1)
#         btn1 = Button(text="Добавить блюдо", size_hint_y=None, height=dp(40))
#         btn1.bind(on_press=self.buttonClicked)
#         box.add_widget(btn1)
#         self.result = Label(text='')
#         box.add_widget(self.result)
#         self.add_widget(box)


def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(StartScreen(name='start_menu'))
sm.add_widget(CoinsCollection(name='coins_collection'))
sm.add_widget(PaperCollection(name='paper_collection'))
sm.add_widget(AddCoin(name='add_coin'))


class CoinsApp(App):
    def __init__(self, **kvargs):
        super(CoinsApp, self).__init__(**kvargs)

        Window.size = (320, 600)
        Window.bottom = True
        # self.config = ConfigParser()

    # def build_config(self, config):
    #     config.adddefaultsection('General')
    #     config.setdefault('General', 'user_data', '{}')

    # def set_value_from_config(self):
    #     self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
    #     self.user_data = ast.literal_eval(self.config.get(
    #         'General', 'user_data'))

    # def get_application_config(self):
    #     return super(CoinsApp, self).get_application_config(
    #         '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    CoinsApp().run()
