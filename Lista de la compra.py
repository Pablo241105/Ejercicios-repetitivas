import flet as ft

def main(page:ft.Page):
    def cambiarColor(e):
        for x in range (1000):
            vCosas[]

        
        page.update()
        
    
    texto=ft.Text(value="ola",color="cyan",size= 150 )
    page.add(texto)
    texto.value="Hola,di tu nombre"
    
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=cambiarColor)
    page.add(bt)
    
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Lexugas")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Tomatoes"))
    page.update()
    
 
    
    page.update()




ft.app(target=main)

