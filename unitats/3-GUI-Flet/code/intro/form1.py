import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Send")
        ])
    )


ft.app(target=main)
