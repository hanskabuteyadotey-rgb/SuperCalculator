from kivy.app import App
from kivy.uix.boxlayout import BoxLayoutkivy.app
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalcApp(App):

    def build(self):

        # Main layout: display on top, buttons underneath
        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        # Calculator display
        self.display = TextInput(
            text="0",
            readonly=True,
            font_size=55,
            halign="right",
            multiline=False,
            size_hint_y=0.25
        )

        main.add_widget(self.display)

        # Buttons
        buttons = GridLayout(
            cols=4,
            spacing=10,
            size_hint_y=0.75
        ){[app]
title = Calculator Pro
package.name = calculatorpro
package.domain = org.yourname
source.dir =.
source.include_exts = py
version = 0.1
requirements = python3,kivy
orientation = portrait
android.api = 34
android.release_artifact = aab

        button_list = [
            "C", "⌫", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=", 
        ]

        for text in button_list:
            btn = Button(
                text=text,
                font_size=35
            )

            btn.bind(on_press=self.button_pressed)
            buttons.add_widget(btn)

        # Add an empty space so the last row looks balanced
        buttons.add_widget(Button(text=""))

        main.add_widget(buttons)

        return main


    def button_pressed(self, instance):

        button = instance.text
        current = self.display.text

        # Clear
        if button == "C":
            self.display.text = "0"

        # Backspace
        elif button == "⌫":
            if len(current) > 1:
                self.display.text = current[:-1]
            else:
                self.display.text = "0"

        # Percentage
        elif button == "%":
            try:
                self.display.text = str(float(current) / 100)
            except:
                self.display.text = "Error"

        # Equals
        elif button == "=":
            try:
                answer = eval(
                    current,
                    {"__builtins__": None},
                    {}
                )

                # Remove .0 from whole numbers
                if isinstance(answer, float) and answer.is_integer():
                    answer = int(answer)

                self.display.text = str(answer)

            except:
                self.display.text = "Error"

        # Operators
        elif button in ["+", "-", "*", "/"]:
            if current[-1:] in ["+", "-", "*", "/"]:
                self.display.text = current[:-1] + button
            else:
                self.display.text += button

        # Decimal
        elif button == ".":
            # Don't allow multiple decimals in one number
            last_number = current.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]

            if "." not in last_number:
                self.display.text += "."

        # Numbers
        else:
            if current == "0" or current == "Error":
                self.display.text = button
            else:
                self.display.text += button


CalcApp().run()
