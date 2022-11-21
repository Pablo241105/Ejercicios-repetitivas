from tkinter import *
from tkinter import ttk
def saludar():
    texto=campoTexto.get()
    textoLabel.set(texto)

    
ventana = Tk()
ventana.title("Ejercicio 1")
ventana.geometry("250x300")
ventana.resizable(width=False,height=False)
ventana.config(background="salmon")


frm = ttk.Frame(ventana).pack()

textoLabel = StringVar()
textoLabel.set("Hola tkinter")
labeltexto=ttk.Label(frm,textvariable=textoLabel)
labeltexto.config(background="gold",border=5,font=("Arial",15))
labeltexto.pack()



campoTexto=ttk.Entry(frm)
campoTexto.pack()

ttk.Button(frm,text="Leer",command=saludar).pack()
ttk.Button(frm,text="Salir",command=ventana.destroy).pack()

ventana.mainloop()