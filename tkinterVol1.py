from tkinter import *
from tkinter import ttk

'''

def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()
'''  

ventana = Tk()

ventana.title("Descargar musica ilegalmente")
ventana.geometry("400x200")
ventana.resizable(width=False,height=False)
ventana.config(background="salmon")

labelTexto=ttk.Label(ventana,text="Pon url").place(x=175 , y=0)



ventana.mainloop()