import flet as ft
import modelo as md


def main(page: ft.Page):

    def guardar_medicamento(e: ft.ControlEvent):
        #tenemos qu ehacer el guardar aqui por que aqui esta el objeto
        nombre = txt_farmaco.value
        farmaco = txt_farmaco.value
        forma_farmaceutica = drp_forma.value
        con_receta = chk_receta.value
        presentacion = txt_pst.value
        unidad = dpt_unidad.value
        categoria = dpt_categoria.value
        dosis = txt_dosis.value
        via = dpt_via.value
        almacenamiento = txt_almto.value
        contraindicaciones = txt_ctnes.value
        efectos = txt_efectos.value
        restricciones = txt_rsnes. value
        md.Medicamento.create(
            nombre = nombre, farmaco=farmaco, forma_farmaceutica=forma_farmaceutica, con_receta=con_receta,
            presentacion=presentacion, unidad = unidad, categoria=categoria, dosis=dosis, via=via, 
            almacenamiento=almacenamiento, contraindicaciones=contraindicaciones, efectos= efectos, restricciones=restricciones
        )
        print("medicamento guardado")




    page.title = "Alta de medicamentos"
    page.theme_mode = "light"  # Cambio de tema

    page.appbar = ft.AppBar(
        leading=ft.Icon("ASSIGNMENT_ADD"), 
        title=ft.Text("Nuevo medicamento"),
        center_title=True,
        bgcolor="green",
        color="white"
    )

    # Componentes de la página
    txt_farmaco = ft.TextField(width=510, label="Nombre del fármaco", autofocus=True)  # Corregí "farmacvo" → "fármaco"
    lista_f= [
        ft.dropdown.Option("Tabletas"), 
        ft.dropdown.Option("Solución inyectable"), 
        ft.dropdown.Option("Crema"), 
        ft.dropdown.Option("Jarabe"),
        ft.dropdown.Option("Cápsulas"),
        ft.dropdown.Option("Suspensión oral"),
        ft.dropdown.Option("Gel"),
        ft.dropdown.Option("Pomada"),
        ft.dropdown.Option("Ungüento"),
        ft.dropdown.Option("Supositorio"),
        ft.dropdown.Option("Parche transdérmico"),
        ft.dropdown.Option("Polvo para reconstituir"),
        ft.dropdown.Option("Aerosol"),
        ft.dropdown.Option("Colirio (solución oftálmica)"),
        ft.dropdown.Option("Enema"),
        ft.dropdown.Option("Grageas"),
        ft.dropdown.Option("Grageas")]#agregar las opciones con chat
    drp_forma = ft.Dropdown(options = lista_f,width=510, label="Forma farmacéutica")  # Corregí "farmaceutica" → "farmacéutica"
    chk_receta = ft.Checkbox(label="Requiere receta", value= True)#cuadirot de palomita
    #se crea fila para dos cajitas de texto
    txt_pst = ft.TextField(width=150, label="Presentación")
    lista_u = [
        ft.dropdown.Option("ml"),
        ft.dropdown.Option("mg"),
        ft.dropdown.Option("g"),
        ft.dropdown.Option("mcg"),
        ft.dropdown.Option("UI"),
        ft.dropdown.Option("mg/ml"),
        ft.dropdown.Option("%")
    ]
    dpt_unidad = ft.Dropdown(options = lista_u,width=130, label="Unidad")

    lista_c = [
        ft.dropdown.Option("Analgésico"),
        ft.dropdown.Option("Antiinflamatorio"),
        ft.dropdown.Option("Antibiótico"),
        ft.dropdown.Option("Antihistamínico"),
        ft.dropdown.Option("Antihipertensivo"),
        ft.dropdown.Option("Anticoagulante"),
        ft.dropdown.Option("Corticosteroide"),
        ft.dropdown.Option("Antidepresivo"),
        ft.dropdown.Option("Antidiabético"),
        ft.dropdown.Option("Antiemético"),
        ft.dropdown.Option("Antifúngico"),
        ft.dropdown.Option("Antivirales"),
        ft.dropdown.Option("Ansiolítico"),
        ft.dropdown.Option("Broncodilatador"),
        ft.dropdown.Option("Anticonvulsivo"),
        ft.dropdown.Option("Antivirales"),
        ft.dropdown.Option("Inmunosupresor"),
        ft.dropdown.Option("Relajante muscular"),
        ft.dropdown.Option("Suplemento vitamínico"),
        ft.dropdown.Option("Antiséptico"),
        ft.dropdown.Option("Antipsicótico")
    ]
    dpt_categoria = ft.Dropdown(options = lista_c, width=210, label="Categoría")

    fila = ft.Row([txt_pst, dpt_unidad, dpt_categoria])

    txt_dosis = ft.TextField(width=250, label="Dosis")
    lista_v = [
        ft.dropdown.Option("Oral"),
        ft.dropdown.Option("Intravenosa(IV)"),
        ft.dropdown.Option("Intramuscular(IM)"),
        ft.dropdown.Option("(IV) ó (IM)"),
        ft.dropdown.Option("Subcutánea(SC)"),
        ft.dropdown.Option("Tópica"),
        ft.dropdown.Option("Oftálmica"),
        ft.dropdown.Option("Nasal"),
        ft.dropdown.Option("Rectal"),
        ft.dropdown.Option("Vaginal"),
        ft.dropdown.Option("Sublingual"),
        ft.dropdown.Option("Inhalatoria"),
        ft.dropdown.Option("Transdérmica")
    ]
    dpt_via = ft.Dropdown(options=lista_v, width=250, label="Vía")
    fila_2 = ft.Row([txt_dosis, dpt_via])

    txt_almto = ft.TextField(width=510, label="Almacenamiento")
    txt_ctnes = ft.TextField(width=510, label="Contraindicaciones")
    txt_efectos = ft.TextField(width=510, label="Efectos")
    txt_rsnes = ft.TextField(width=510, label="Restricciones")

    btn_guardar = ft.ElevatedButton(
        text = "Guardar",
        icon = "SAVE_ALT",
        bgcolor = "blue",
        color = "white",
        icon_color="white",
        width = 150,
        on_click= guardar_medicamento
    )
    btn_cancelar = ft.ElevatedButton(
        text = "Cancelar",
        icon = "CANCEL_PRESENTATION",
        bgcolor = "red",
        color = "white",
        icon_color="white",
        width = 150
    )
    fila_3 = ft.Row([btn_guardar, btn_cancelar], alignment='center')
    # Agregar los componentes a la página
    page.add(txt_farmaco, drp_forma, chk_receta, fila, fila_2, txt_almto, txt_ctnes, txt_efectos, txt_rsnes, fila_3)

    page.update()  # Actualiza la página

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
