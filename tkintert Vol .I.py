from tkinter import *
from tkinter import ttk
ventana = Tk()
ventana.title("Ejercicio 1")
ventana.geometry("600x500")
ventana.resizable(width=False,height=False)
ventana.config(background="bisque2")
ventana.iconbitmap(file="cosa.ico")
frm = ttk.Frame(ventana).pack()
labeltexto=ttk.Label(frm,text="Hola Tkinter")
labeltexto.config(background="dark slate grey",border=5,font=("Arial",15))
labeltexto.pack()

ttk.Button(frm,text="Salir",command=ventana.destroy).pack()

ventana.mainloop()