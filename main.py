from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class AppleDoctor(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        lbl = Label(text='Apple Doctor\nDeveloper: Rahil Afzal', 
                    font_size='30sp', halign='center')
        layout.add_widget(lbl)
        return layout

if __name__ == '__main__':
    AppleDoctor().run()
