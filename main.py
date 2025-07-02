import flet as ft
import consulta_airtable as cat
import consultas as cm
import alta_medicamentos as alta_medicamentos


def main(page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)

    def mostrar_medicamentos(e: ft.ControlEvent):
        page.clean()
        cm.main(page)
        

    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title = ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )

    btn_interacciones = ft.FilledButton(
        content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="BLUEGREY500"),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER)
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding = 10,
            height=100
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.Border(1, "green")
        ),
        bgcolor="GREEN200",
        color="black",
        width=200,
        on_click=mostrar_interacciones
    )

    btn_medicamento = ft.FilledButton(
        content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("MEDICATION_OUTLINED", size=40, color="BLUEGREY700"),
                    ft.Text("Nuevo medicamento", text_align=ft.TextAlign.CENTER)
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding = 10,
            height=100
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.Border(1, "green")
        ),
        bgcolor="GREEN300",
        color="black",
        width=200
    )

    btn_lista = ft.FilledButton(
        content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("FEATURED_PLAY_LIST", size=40, color="BLUEGREY900"),
                    ft.Text("Lista de medicamentos", text_align=ft.TextAlign.CENTER)
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding = 10,
            height=100
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.Border(1, "green")
        ),
        bgcolor="GREEN400",
        color="black",
        width=200,
        on_click=mostrar_medicamentos
    )

    btn_container = ft.Container(
    content=ft.Row(
        controls=[
            btn_interacciones,
            btn_medicamento,
            btn_lista
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    ),
    alignment=ft.alignment.center
)

    page.add(ft.Divider(color="black"), btn_container)
    page.update()
    #nuevo medicamento y listado de medicamentos

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
#flet tun -w main.py