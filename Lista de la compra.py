import flet as ft
vCosas=[]
def main(page:ft.Page):
    def guardardatos(e):
      vCosas=[]
      vCosas.append(dropDown_Menu)
      print(guardardatos())
       
    texto=ft.Text(value="hola",color="cyan",size= 50 )
    page.add(texto)
    texto.value="Hola,muestra tu compra"
    
    bt=ft.FloatingActionButton(icon=ft.icons.ADD,on_click=guardardatos)
    page.add(bt)
    img = ft.Image(src=f"img/logo.png", width=300, height=300)
    
    
    page.add(img)
    textField_Nombre=ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    print(textField_Nombre)
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Manzanas")])
    page.add(dropDown_Menu)
    page.update()
    page.add(ft.Text("¿Cuantos kilos quieres de esto?:"),
        ft.Slider(min=0, max=50, divisions=50, label="{value}"))
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Peras")])
    page.add(dropDown_Menu)
    page.update()
    page.add(ft.Text("¿Cuantos kilos quieres de esto?:"),
        ft.Slider(min=0, max=50, divisions=50, label="{value}")) 
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Melones")])
    page.add(dropDown_Menu)
    page.update()
    page.add(ft.Text("¿Cuanto quieres de esto?:"),
        ft.Slider(min=0, max=50, divisions=50, label="{value}")) 
    dropDown_Menu=ft.Dropdown(width=100,options=[ft.dropdown.Option("Patatas")])
    page.add(dropDown_Menu)
    page.update()
    page.add(ft.Text("¿Cuantos kilos quieres de esto?:"),
        ft.Slider(min=0, max=50, divisions=50, label="{value}")) 
    
ft.app(target=main,
        assets_dir="recursos")

 