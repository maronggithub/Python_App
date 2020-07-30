from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screenmanager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
  pass

class RootWidget(Screenmanager):
  pass

class MainApp(App):
  def build(self):
    return RootWidget()


if __name__ == "__main__":
  MainApp().run()
