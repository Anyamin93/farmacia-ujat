import flet as ft
import modelo as md

def main(page: ft.Page):

    def actualizar_datos(e: ft.ControlEvent):
        nombre = drp_medicamentos.value.strip()
        if nombre == "":
            return
        
        medicamento = md.Medicamento.select().where(md.Medicamento.descripcion == nombre).first()

        if medicamento:
            txt_clave.value = medicamento.clave
            txt_presentacion.value = medicamento.presentacion
            txt_clasificacion.value = medicamento.clasificacion
            txt_nivel_atencion.value = medicamento.nivel_atencion
            txt_farmaco.value = medicamento.nombre_farmaco
            page.update()

    def borrar_medicamento(e: ft.ControlEvent):
        nombre = drp_medicamentos.value.strip()

        if nombre == "":
            snack_bar = ft.SnackBar(ft.Text("Introduce el nombre"))
            page.open(snack_bar)
            return

        md.Medicamento.delete().where(md.Medicamento.descripcion == nombre).execute()
        snack_bar = ft.SnackBar(ft.Text("Borrado"), bgcolor="blue", show_close_icon=True)
        page.open(snack_bar)

        txt_clave.value = ""
        txt_presentacion.value = ""
        txt_clasificacion.value = ""
        txt_nivel_atencion.value = ""
        txt_farmaco.value = ""
        drp_medicamentos.value = ""
        page.update()

    page.title = "Baja de medicamentos (UJAT)"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        leading=ft.Icon(name='folder_delete_sharp', color=ft.colors.WHITE),
        title=ft.Text("Baja medicamento"),
        bgcolor="green",
        color="white"
    )

    lista = []
    medicamentos = md.Medicamento.select(md.Medicamento.descripcion).distinct()

    for med in medicamentos:
        lista.append(ft.dropdown.Option(med.descripcion))

    drp_medicamentos = ft.Dropdown(
        options=lista,
        width=550,
        label="Nombre del medicamento",
        on_change=actualizar_datos
    )

    txt_clave = ft.TextField(width=250, border="underline", filled=True, label="Clave", read_only=True)
    txt_presentacion = ft.TextField(label="Presentación", multiline=True, min_lines=1, max_lines=3, read_only=True)
    txt_clasificacion = ft.TextField(width=550, label="Clasificación", read_only=True)
    txt_nivel_atencion = ft.TextField(width=550, label="Nivel de atención", read_only=True)
    txt_farmaco = ft.TextField(width=550, label="Fármaco o sustancia activa", read_only=True)

    btn_Borrar = ft.Container(
        content=ft.ElevatedButton(
            text="Borrar",
            icon="delete_forever_rounded",
            icon_color="white",
            bgcolor="red",
            color="white",
            width=150,
            on_click=borrar_medicamento
        ),
        alignment=ft.alignment.center
    )

    page.add(
        drp_medicamentos,
        txt_clave,
        txt_presentacion,
        txt_clasificacion,
        txt_nivel_atencion,
        txt_farmaco,
        btn_Borrar
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

    
