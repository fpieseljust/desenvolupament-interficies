import flet as ft


class ContainerID(ft.Container): # Heredem de Container
    def __init__(self, id: str):
        super().__init__()
        self.id = id # Definim la propietat id

        # Per defecte el creem amb l'identificador centrat, 
        # color de fons AMBER, tamany 150x150 i arredonit
        self.content = ft.Text(id)
        self.alignment=ft.alignment.center
        self.width = 150
        self.height = 150
        self.border_radius = 5
        self.bgcolor = ft.colors.AMBER
        


def main(page: ft.Page):
    container_id = ContainerID("Identificador")
    container_id.on_click = container_clicked
    page.add(container_id)
    page.update()


def container_clicked(e):
    print(e.control.id) # Accedim a la propietat que hem definit


ft.app(target=main)
