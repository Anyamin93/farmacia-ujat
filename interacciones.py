import flet as ft
import modelo as md
import nube as nb

def main(page: ft.Page):
    def mostrar_interacciones(e: ft.ControlEvent):
        if e.control == dpt_medicamento1:#que componente lanzo el evento
            desc = dpt_medicamento1.value
            txt = txt_interaccion1
        elif e.control == dpt_medicamento2:
            desc = dpt_medicamento2.value
            txt = txt_interaccion2
        elif e.control == dpt_medicamento3:
            desc = dpt_medicamento3.value
            txt = txt_interaccion3
        elif e.control == dpt_medicamento4:
            desc = dpt_medicamento4.value
            txt = txt_interaccion4
        #consultar las interacciones
        med = md.Medicamento.get(
            md.Medicamento.descripcion == desc
            )
        #si el medicamento no tiene farmaco asociado
        if med.nombre_farmaco is None:
            txt.value = "No tiene en la BD"
        else:
            txt.value = med.nombre_farmaco.interacciones
            #actualziar caja de texto
        txt.update()    

    def guardar_receta(e: ft.ControlEvent):
        #validar_campos de entrada
        if dpt_medicamento1.value is None:
            snack_bar = ft.SnackBar(
                content = ft.Text("Selecciona el primer medicamento"),
                bgcolor = "red",
                show_close_icon = True
            )
            page.open(snack_bar)
            return
        #guardar el medicamento
        med1 = nb.Receta(
            medicamento = dpt_medicamento1.value,
            interacciones = txt_interaccion1.value
        )
        med1.save()
        snack_bar = ft.SnackBar(
            content  =ft.Text("Éxito"),
            bgcolor="blue",
            show_close_icon = True
        )
        page.open(snack_bar)



    page.title = "Interacciones medicamentosas"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
    title = ft.Text("Interacciones UJAT", weight="bold", size=28, font_family="Courier New"),
    leading = ft.Icon("medical_services"),
    bgcolor = "purple",
    color = "white",
    center_title = True
    )

    txt_medicamentos = ft.Text("Medicamentos", weight="bold", size=18, font_family="Courier New")
    div_medicamentos = ft.Divider(thickness=2, color="white")

    lista = []
    for m in md.Medicamento.select():
        elemento = ft.dropdown.Option(m.descripcion)
        lista.append(elemento)

    dpt_medicamento1 = ft.Dropdown(options = lista, editable = True, enable_filter = True, label = "Seleccione medicamento 1", 
    on_change=mostrar_interacciones)
    dpt_medicamento2 = ft.Dropdown(options = lista, editable = True, enable_filter = True, label = "Seleccione medicamento 2",
    on_change=mostrar_interacciones)
    dpt_medicamento3 = ft.Dropdown(options = lista, editable = True, enable_filter = True, label = "Seleccione medicamento 3",
    on_change=mostrar_interacciones)
    dpt_medicamento4 = ft.Dropdown(options = lista, editable = True, enable_filter = True, label = "Seleccione medicamento 4",
    on_change=mostrar_interacciones)

    col_medicamentos = ft.Column(
        [txt_medicamentos, div_medicamentos, dpt_medicamento1, dpt_medicamento2, dpt_medicamento3, dpt_medicamento4], expand=True, spacing= 20)

    txt_interacciones = ft.Text("Interacciones", weight="bold", size=18, font_family="Courier New")
    div_interacciones = ft.Divider(thickness=2, color="white")

    txt_interaccion1 = ft.TextField(label = "Interacciones medicamento 1", read_only = True)
    txt_interaccion2 = ft.TextField(label = "Interacciones medicamento 2", read_only = True)
    txt_interaccion3 = ft.TextField(label = "Interacciones medicamento 3", read_only = True)
    txt_interaccion4 = ft.TextField(label = "Interacciones medicamento 4", read_only = True)

    col_interacciones = ft.Column(
        [txt_interacciones, div_interacciones, txt_interaccion1, txt_interaccion2, txt_interaccion3, txt_interaccion4], expand=True, spacing=20)

    row_componentes = ft.Row([col_medicamentos, col_interacciones], spacing=20)

    btn_aceptar = ft.ElevatedButton(text="Guardar", icon="Cloud", bgcolor="green", color="white", icon_color="white", width=150, on_click=guardar_receta)

    btn_cancelar = ft.ElevatedButton(text="Cerrar", icon="close", bgcolor="red", color="white", icon_color="white", width=150)

    row_botones = ft.Row([btn_aceptar, btn_cancelar], alignment="end", spacing=20)

    page.add(row_componentes, row_botones)
#punto de inicio de la aplicacion
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)