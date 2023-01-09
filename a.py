import flet as ft

def main(page: ft.Page):
    page.title = "Images Example"
    

    img = ft.Image(src=f"img/logo.png", width=200, height=200)
    

    page.add(img)

ft.app(target=main,
        assets_dir="recursos")
