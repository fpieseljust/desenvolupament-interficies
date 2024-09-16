import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Ruta inicial: {page.route}"))

ft.app(target=main, view='web_browser', port=8080)