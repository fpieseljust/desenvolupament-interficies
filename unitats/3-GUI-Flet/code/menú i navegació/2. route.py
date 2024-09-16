import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Ruta inicial: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Nova ruta: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(target=main, view='web_browser', port=8080)