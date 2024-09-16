import flet as ft

def main(page: ft.Page):
    page.title = "ListView"

    listview = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    page.add(listview)

    for i in range(0, 60):
        listview.controls.append(ft.Text(f"Element {i}"))
        
    page.update()

ft.app(target=main, view='web_browser', port=8550)