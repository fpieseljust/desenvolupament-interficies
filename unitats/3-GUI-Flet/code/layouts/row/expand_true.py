import flet as ft

def main(page: ft.Page):
    row = ft.Row([
        ft.TextField(hint_text="Enter your name", expand=True),
        ft.ElevatedButton(text="Join chat")
        ])

    page.add(
        row
    )


ft.app(target=main)