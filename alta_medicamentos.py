import flet as ft
import modelo as md

def main(page: ft.Page):

    def guardar_medicamento(e: ft.ControlEvent):
        clave = txt_clave.value.strip()
        nombre = txt_descripcion.value.strip()
        presentacion = txt_presentacion.value.strip()
        clasificacion = drp_clasificacion.value
        nivel = drp_nivel_atencion.value
        farmaco = drp_farmaco.value

        #Validar campos
        if clave == "":
            snack_bar = ft.SnackBar(ft.Text("Introduce la clave"))
            page.open(snack_bar)
            return
        if nombre == "":
            snack_bar = ft.SnackBar(ft.Text("Introduce el nombre"))
            page.open(snack_bar)
            return
        if presentacion == "":
            snack_bar = ft.SnackBar(ft.Text("Introduce la presentación"))
            page.open(snack_bar)
            return
        if clasificacion == None:
            snack_bar = ft.SnackBar(ft.Text("Introduce la clasificación"))
            page.open(snack_bar)
            return
        if nivel == None:
            snack_bar = ft.SnackBar(ft.Text("Introduce el nivel de atención"))
            page.open(snack_bar)
            return

        #guardar medicamento en la base de datos
        md.Medicamento.create(
            clave = clave,
            descripcion = nombre,
            presentacion = presentacion,
            clasificacion = clasificacion,
            nivel_atencion = nivel,
            nombre_farmaco = farmaco
        )
        snack_bar = ft.SnackBar(ft.Text("Guardado"), bgcolor="blue", show_close_icon=True)
        page.open(snack_bar)



    # Configuración de la página
    page.title = "Alta de medicamentos (UJAT)"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        leading=ft.Icon('MEDICAL_SERVICES', color=ft.Colors.WHITE),
        title=ft.Text("Nuevo medicamento"),
        bgcolor="green",
        color="white"
    )
    
    # Componentes de la página 
    txt_clave = ft.TextField(width= 250, border= "underLine", filled= True, label="Clave")
    txt_descripcion = ft.TextField(label="Nombre y descripcion del medicamento",
    multiline=True, 
    min_lines=1, 
    max_lines=3
    )
    txt_presentacion = ft.TextField(label="Presentación",multiline=True, min_lines=1, max_lines=3) 
    
    lista = []
    medicinas = md.Medicamento.select(md.Medicamento.clasificacion).distinct()
    for med in medicinas:
        lista.append(ft.dropdown.Option(med.clasificacion))
    
    drp_clasificacion = ft.Dropdown(options=lista, width=550, label="Clasificación")
    
    lista = [ft.dropdown.Option("Nivel 1"),
             ft.dropdown.Option("Nivel 2"),
             ft.dropdown.Option("Nivel 3"),
             ft.dropdown.Option("Nivel 1 y 2"),
             ft.dropdown.Option("Nivel 1 y 3"),
             ft.dropdown.Option("Nivel 2 y 3"),
             ft.dropdown.Option("Todas las anteriores")
    ]

    drp_nivel_atencion = ft.Dropdown(options=lista, width=550, label="Nivel de atención")

    lista = []
    farmacos = md.Farmaco.select(md.Farmaco.nombre).distinct()

    for far in farmacos:
        lista.append(ft.dropdown.Option(far.nombre))

    drp_farmaco = ft.Dropdown(options=lista, width=550, label="Fármaco o sustancia activa")
    
    
    btn_guardar = ft.ElevatedButton(
        text="Guardar",
        icon="save",
        icon_color="white",
        bgcolor="blue",
        color="white", 
        width=150,
        on_click= guardar_medicamento
    )
    btn_cancelar = ft.ElevatedButton(
        text="Cancelar",
        icon="cancel",
        icon_color="white",
        bgcolor="red",
        color="white",
        width=150
    )
    fila2 = ft.Row([btn_guardar, btn_cancelar], alignment='center')
    
    # Agregar los componentes a la página 
    page.add(txt_clave, txt_descripcion,  txt_presentacion, drp_clasificacion, drp_nivel_atencion,drp_farmaco, fila2)
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)