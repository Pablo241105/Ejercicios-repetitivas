from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Pedir datos al usuario")
ventana.geometry("300x300")
ventana.resizable(False,False)
ventana.config(background="gold")

labelTexto=ttk.Label(ventana,text="Pon tus datos")


labelusuario=ttk.Label(ventana,text="Introduce tu usuario")
entryusuario=ttk.Entry(ventana)
labelcontraseña=ttk.Label(ventana,text="Intruce tu contraseña")
entrycontraseña=ttk.Entry(ventana)

botonguardar=ttk.Button(ventana,text="Guardar")
botonsalir=ttk.Button(ventana,text="Salir")


labelTexto.grid(row=0,column=1)
labelusuario.grid(row=1,column=0)
entryusuario.grid(row=1,column=1)

labelcontraseña.grid(row=3,column=0)
entrycontraseña.grid(row=3,column=1)

botonguardar.grid(row=4,column=1)
botonsalir.grid(row=4,column=0)
ventana.mainloop()