import flet as ft
import modelo as md


def main(page: ft.Page):

    page.title = "Filtro de medicamentos (UJAT)"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        leading=ft.Icon('FILTER_ALT', color=ft.Colors.WHITE),
        title=ft.Text("Medicamentos"),
        center_title=True,
        bgcolor="green",
        color="white"
    )


    txt_medicamento = ft.Text("Medicamentos", size = 15)

    linea = ft.Divider(thickness=1, color=ft.Colors.GREEN)

    lista = []
    medicina = md.Medicamento.select(md.Medicamento.descripcion).distinct()
    for med in medicina:
        lista.append(ft.dropdown.Option(med.descripcion))

    drp_medi1 = ft.Dropdown(options=lista, 
    width=1250, 
    label="Medicamento 1", 
    editable=True, 
    enable_filter=True)


    drp_medi2 = ft.Dropdown(options=lista, 
    width=1250, 
    label="Medicamento 2", 
    editable=True,
    enable_filter=True)

    page.add(txt_medicamento, linea, drp_medi1, drp_medi2)
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)