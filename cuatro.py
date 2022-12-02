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
    page.update()







ft.app(target=main,)

        
        
