import flet as ft


class Counter(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.text = ft.Text(str(self.counter))

    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def subtract_click(self, e):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        return ft.Row([ft.IconButton(ft.icons.REMOVE, on_click=self.subtract_click),
         self.text, ft.IconButton(ft.icons.ADD, on_click=self.add_click)])


def main(page):
    counter = Counter()
    counter.counter = 0
    page.add(counter)


ft.app(target=main)
