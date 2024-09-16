import time

import flet as ft

def main(page: ft.Page):
    t = ft.Text()
    page.add(t)

    for i in range(10):
        t.value = f"Pas número {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)
