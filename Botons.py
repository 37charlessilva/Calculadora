from dataclasses import field

import flet as ft

class MyButton(ft.Button):

    def __init__(self, text: str, on_click, bgcolor: str, color: str):
        super().__init__(
            text,
            on_click = on_click,
            bgcolor = bgcolor,
            color = color,
        )
        
        self.expand = 1
        

class DigitButton(MyButton):
    def __init__(self, text: str, result):
        self.text = text 

        super().__init__(
            text=text, 
            bgcolor=ft.Colors.WHITE_24, 
            on_click=lambda e: self.clickDigit(e, result),
            color=ft.Colors.WHITE
        )

        if text == "0":
            self.expand = 2
        
    def clickDigit(self, e, result):
        if result.value == "0":
            result.value = self.text
        else:
            result.value += self.text

        e.page.update()


class ActionButton(MyButton):
    def __init__(self, text: str, on_click):
        super().__init__(
            text=text, 
            on_click=on_click, 
            bgcolor=ft.Colors.ORANGE, 
            color=ft.Colors.WHITE
        )


class ExtraActionButton(MyButton):
    def __init__(self, text: str, on_click):
        super().__init__(
            text=text, 
            on_click=on_click, 
            bgcolor=ft.Colors.BLUE_GREY_100, 
            color=ft.Colors.BLACK
        )