from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ControlMenu(GridLayout):

    def __init__(self, home_action):
        super(ControlMenu, self).__init__(cols=4, height=20, size_hint=(1, 1))

        self.home_action = home_action
        back_button = Button(text='ДОМОЙ',
                             on_press=self.home_action,
                             size_hint_y=None)

        back_button2 = Button(text='ДОМОЙ',
                             on_press=self.home_action,
                             size_hint_y=None)

        self.add_widget(back_button)
        self.add_widget(back_button2)

