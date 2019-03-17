from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp



class ControlMenu(GridLayout):

    def __init__(self, home_action, add_action):
        super(ControlMenu, self).__init__(cols=4)

        self.home_action = home_action
        self.add_action = add_action

        back_button = Button(text='ДОМОЙ',
                             on_press=self.home_action,
                             height=dp(40),
                             size_hint_y=None)

        add_button = Button(text=' + ', on_press=self.add_action,
                            size_hint_y=None, height=40)

        self.add_widget(back_button)
        self.add_widget(add_button)

