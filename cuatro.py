import flet as ft

def main(page:ft.Page):
    def cambiarColor(e):
        for x in range (10):
            text=ft.Text(value=f"Texto numero {x}",size=10)
            page.add(text)
        
        
        page.update()  
        
    
    texto=ft.Text(value="ola",color="cyan",size= 150 )    
    page.add(texto) 
    texto.value="Hola"
    
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=cambiarColor)
    page.add(bt)
    
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Si")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("No"))
    page.update()
    
    slider_edad=ft.Slider(min=0,max=120,divisions=120,label=f"Edad:{value}")
    page.add(slider_edad)
    
    page.update()




ft.app(target=main)

