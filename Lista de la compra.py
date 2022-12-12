import flet as ft
vCosas=[]
def main(page:ft.Page):
    def guardardatos(e):
      vCosas=[]
      vCosas.append(Cosa2)
      vCosas.append(Cosa3)
      vCosas.append(Cosa4)
      vCosas.append(Cosa5)
      print(vCosas)
       
        
    texto=ft.Text(value="hola",color="cyan",size= 150 )
    page.add(texto)
    texto.value="Hola,di tu nombre"
    
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=guardardatos)
    page.add(bt)
    
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    print(textField_Nombre)
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Cosa 1")])
    page.add(dropDown_Menu)
    Cosa2=dropDown_Menu.options.append(ft.dropdown.Option("Cosa 2"))
    Cosa3=dropDown_Menu.options.append(ft.dropdown.Option("Cosa 3"))
    Cosa4=dropDown_Menu.options.append(ft.dropdown.Option("Cosa 4"))
    Cosa5=dropDown_Menu.options.append(ft.dropdown.Option("Cosa 5"))
    page.update()
    
    
    page.update()

ft.app(target=main)