import flet as ft


def main(page: ft.Page):
    row = ft.Row([
        ft.Container(border=ft.border.all(1), expand=1, content=ft.Text(
            "expand = 2", text_align=ft.TextAlign.CENTER)),
        ft.Container(border=ft.border.all(1), expand=3, content=ft.Text(
            "expand = 3", text_align=ft.TextAlign.CENTER)),
        ft.Container(border=ft.border.all(1), expand=1, content=ft.Text(
            "expand = 1", text_align=ft.TextAlign.CENTER))
    ])

    page.add(
        row
    )


ft.app(target=main)
