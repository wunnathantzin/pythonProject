from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

_author_ = 'Tom'


class ConvertkmApp(App):
    def build(self):
        Window.size = (200, 200)
        self.title = "Convert KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment_add(self, convert):
        self.value = convert + 1
        print(self.value)
    def handle_increment_sub(self, convert):
        self.value = convert - 1
        print(self.value)
ConvertkmApp().run()