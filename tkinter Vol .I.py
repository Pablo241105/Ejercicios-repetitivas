from tkinter import *
from tkinter import ttk
def saludar():
    texto=campoTexto.get()
    print(texto)

    
ventana = Tk()
ventana.title("Ejercicio 1")
ventana.geometry("250x300")
ventana.resizable(width=False,height=False)
ventana.config(background="cyan")


frm = ttk.Frame(ventana).pack()


labeltexto=ttk.Label(frm,text="Hola Tkinter")
labeltexto.config(background="gold",border=5,font=("Arial",15))
labeltexto.pack()



campoTexto=ttk.Entry(frm)
campoTexto.pack()

ttk.Button(frm,text="Leer",command=saludar).pack()
ttk.Button(frm,text="Salir",command=ventana.destroy).pack()

ventana.mainloop()