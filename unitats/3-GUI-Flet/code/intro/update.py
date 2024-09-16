import time

import flet as ft

def main(page: ft.Page):
    t = ft.Text()
    page.add(t)

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(1)

ft.app(target=main)