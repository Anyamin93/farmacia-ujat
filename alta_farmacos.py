import flet as ft
import modelo as md

def main(page: ft.Page):

    def guardar_farmaco(e: ft.ControlEvent):
        #selecciona todos los farmacos donde sean igual al nombre actual y obtiene el primero de los resultados
        farmaco_existente = md.Farmaco.select().where(md.Farmaco.nombre == txt_nombre.value).first()
        if farmaco_existente:
            snack_bar = ft.SnackBar(
                content = ft.Text("El fármaco ya existe"),
                bgcolor = "red",
                show_close_icon = True
            )
            page.open(snack_bar)
            return

        nombre = txt_nombre.value
        descripcion = txt_descripcion.value
        categoria = txt_categoria.value
        interacciones = txt_interacciones.value
        md.Farmaco.create(
            nombre = nombre, descripcion=descripcion, categoria=categoria,
            interacciones = interacciones
        )
        print("Farmaco guardado")
        snack_bar = ft.SnackBar(
            content  =ft.Text("Fármaco guardado"),
            bgcolor="blue",
            show_close_icon = True
        )
        page.open(snack_bar)

    # Configuración de la página
    page.title = "Alta de Fármacos (UJAT)"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        leading=ft.Icon('MEDICAL_SERVICES', color=ft.colors.WHITE),
        title=ft.Text("Nuevo fármaco"),
        bgcolor="green",
        color="white"
    )
    
    # Componentes de la página 
    txt_nombre = ft.TextField(width= 550, border= "underLine", filled= True, label="nombre")
    txt_descripcion = ft.TextField(width= 550, label="Descripcion del fármacos",
    multiline=True, 
    min_lines=1, 
    max_lines=3
    )
    txt_categoria = ft.TextField(label="Categoría",multiline=True) 

    txt_interacciones = ft.TextField(width= 550,label="Interacciones",multiline=True, min_lines=1, max_lines=3)
    
    btn_guardar = ft.ElevatedButton(
        text="Guardar",
        icon="save",
        icon_color="white",
        bgcolor="blue",
        color="white", 
        width=150,
        on_click=guardar_farmaco
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
    page.add(txt_nombre, txt_descripcion,  txt_categoria, txt_interacciones, fila2)
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)