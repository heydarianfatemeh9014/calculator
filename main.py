from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

# برای تست روی کامپیوتر، اندازه رو مثل گوشی می‌کنیم (مثلا 360x640)
Window.size = (360, 640)

KV = """
BoxLayout:
    orientation: "vertical"

    MDTextField:
        id: solution
        text: ""
        halign: "right"
        font_size: "40sp"
        readonly: True
        size_hint_y: 0.2
        mode: "rectangle"
        line_color_focus: 1,1,1,0
        hint_text: "0"
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        md_bg_color: 0.1,0.1,0.1,1

    MDGridLayout:
        cols: 4
        adaptive_height: True
        spacing: dp(10)
        padding: dp(10)
        
        MDFillRoundFlatButton:
            text: "7"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "8"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "9"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "/"
            md_bg_color: 1,0.5,0.2,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "4"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "5"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "6"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "*"
            md_bg_color: 1,0.5,0.2,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "1"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "2"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "3"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "-"
            md_bg_color: 1,0.5,0.2,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "0"
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "."
            md_bg_color: 0.2,0.6,0.8,1
            on_release: app.button_press(self.text)

        MDFillRoundFlatButton:
            text: "C"
            md_bg_color: 1,0.3,0.3,1
            on_release: app.clear()

        MDFillRoundFlatButton:
            text: "+"
            md_bg_color: 1,0.5,0.2,1
            on_release: app.button_press(self.text)

    MDFillRoundFlatButton:
        text: "="
        size_hint_y: 0.2
        font_size: "35sp"
        md_bg_color: 0.1,0.8,0.1,1
        pos_hint: {"center_x": 0.5}
        on_release: app.calculate()
"""


class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # تم دارک
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def button_press(self, text):
        if self.root.ids.solution.text == "Error":
            self.root.ids.solution.text = ""
        self.root.ids.solution.text += text

    def clear(self):
        self.root.ids.solution.text = ""

    def calculate(self):
        try:
            self.root.ids.solution.text = str(eval(self.root.ids.solution.text))
        except:
            self.root.ids.solution.text = "Error"


if __name__ == "__main__":
    CalculatorApp().run()
