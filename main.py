import flet as ft
import random

def main(page: ft.Page):

    def number():
        ran_number = random.randint(0, 99)
        return ran_number

    def update_number(e):
        text.value = f"O número sorteado foi: {number()}"
        page.update()

    text = ft.Text(f"O número sorteado foi: {number()}", size=30, text_align="center")
    button = ft.ElevatedButton(text='Sortear outro número', on_click=update_number)
    
    layout = ft.Column(
        [text, button],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)


    page.add(
        ft.Container(
            content=layout,
            alignment=ft.alignment.center,
            expand=True))

ft.app(main)
