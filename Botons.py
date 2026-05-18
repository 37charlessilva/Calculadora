from dataclasses import field

import flet as ft

class MyButton(ft.Button):

    def __init__(self, text, bgcolor: str, color: str, result):
        super().__init__(
            text,
            on_click = lambda e: self.click(e, result, text),
            bgcolor = bgcolor,
            color = color,
        )
        
        self.expand = 1
        
    def click(self, e, result, text):
        if result.value == "0":
            result.value = text
        else:
            result.value += str(text)

        e.page.update()
    

class DigitButton(MyButton):
    def __init__(self, text: str, result):

        super().__init__(
            text=text, 
            bgcolor=ft.Colors.WHITE_24, 
            result=result,
            color=ft.Colors.WHITE
        )


class ActionButton(MyButton):
    def __init__(self, text: str, result):
        super().__init__(
            text=text, 
            result=result, 
            bgcolor=ft.Colors.ORANGE, 
            color=ft.Colors.WHITE
        )

    def click(self, e, result, text):
        if text == "=":
            if result.value != "0":
                label = str(result.value).replace("^", "**")
                result.value = str(eval(label))
        
        elif text == "⬅️":
            result.value = result.value[:-1]

        else:
        
            return super().click(e, result, text)
        
        e.page.update()

class ExtraActionButton(MyButton):
    def __init__(self, text: str, result):
        super().__init__(
            text=text, 
            result=result, 
            bgcolor=ft.Colors.BLUE_GREY_100, 
            color=ft.Colors.BLACK
        )

    def click(self, e, result, text):
        if text == "AC":

            result.value = "0"
            e.page.update()
            
        else:

            return super().click(e, result, text)