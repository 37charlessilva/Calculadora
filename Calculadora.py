from dataclasses import field
from Botons import DigitButton, ActionButton, ExtraActionButton
import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora"
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(controls=[
                        ExtraActionButton(text="AC", result=result), 
                        ExtraActionButton(text="^", result=result),
                        ExtraActionButton(text="%", result=result),
                        ActionButton(text="/", result=result),
                        ]  
                    ),
                    ft.Row(controls=[
                        DigitButton(text="7", result=result), 
                        DigitButton(text="8", result=result),
                        DigitButton(text="9", result=result), 
                        ActionButton(text="*", result=result),
                        ]
                    ),
                    ft.Row(controls=[
                        DigitButton(text="4", result=result),
                        DigitButton(text="5", result=result),
                        DigitButton(text="6", result=result),
                        ActionButton(text="-", result=result),
                        ]
                    ),
                    ft.Row(controls=[
                        DigitButton(text="1", result=result),
                        DigitButton(text="2", result=result),
                        DigitButton(text="3", result=result),
                        ActionButton(text="+", result=result),
                        ]
                    ),
                    ft.Row(controls=[
                        DigitButton(text="0", result=result),
                        DigitButton(text=".", result=result),
                        ActionButton(text="⬅️", result=result), 
                        ActionButton(text="=", result=result), 
                        ]
                    ),
                ],
            )
        )
    )
    

    

if __name__ == "__main__":
    ft.run(main)