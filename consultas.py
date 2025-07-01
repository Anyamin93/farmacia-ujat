import flet as ft
import modelo as md

def main(page: ft.Page):
#Configuara pagina
    page.title = "consultas"
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title= ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("LIST_ALT", color=ft.Colors.WHITE),
        bgcolor="blue",
        center_title=True,
    )

#Compomponentes de la pagina
    encabezado = [
        ft.DataColumn(ft.Text("Descripción", width=200)),
        ft.DataColumn(ft.Text("Presentación", width=200)),
        ft.DataColumn(ft.Text("Clasificación", width=200)),
        ft.DataColumn(ft.Text("Nivel de atencion", width=100)),
        ft.DataColumn( ft.Text("Sustanacia activa", width=200))
    ]
    filas = []
    medicinas = md.Medicamento.select()
    for med in medicinas:
        celda1 = ft.DataCell(ft.Text(med.descripcion,weight="bold"))
        celda2 = ft.DataCell(ft.Text(med.presentacion))
        celda3 = ft.DataCell(ft.Text(med.clasificacion,italic=True))
        celda4 = ft.DataCell(ft.Text(med.nivel_atencion))
        celda5 = ft.DataCell(ft.Text(med.descripcion,color="pink"))   
        fila = ft.DataRow([celda1,celda2,celda3,celda4,celda5])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_medicamentos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)