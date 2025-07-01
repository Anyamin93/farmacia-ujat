import flet as ft
import modelo as md

def main(page: ft.Page):
#Configuara pagina
    page.title = "Consultas de Fármacos"
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title= ft.Text("Listado de fármacos UJAT"),
        leading=ft.Icon("LIST_ALT", color=ft.Colors.WHITE),
        bgcolor="blue",
        center_title=True,
    )

#Compomponentes de la pagina
    encabezado = [
        ft.DataColumn(ft.Text("Nombre", width=250)),
        ft.DataColumn(ft.Text("Descripcion", width=400)),
        ft.DataColumn(ft.Text("Categoria", width=200)),
        ft.DataColumn(ft.Text("Interacciones", width=400))
    ]
    filas = []
    farmacos = md.Farmaco.select()
    for far in farmacos:
        celda1 = ft.DataCell(ft.Text(far.nombre, weight="bold"))
        celda2 = ft.DataCell(ft.Container(content=ft.Text(far.descripcion, selectable=True, no_wrap=True),width=400))
        celda3 = ft.DataCell(ft.Text(far.categoria))
        celda4 = ft.DataCell(ft.Container(content=ft.Text(far.interacciones, selectable=True, no_wrap=True),width=400))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)

    tbl_farmacos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_farmacos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)