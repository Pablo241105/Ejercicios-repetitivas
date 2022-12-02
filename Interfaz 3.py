from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usuario=""
contraseña=""
confirmar=""
vUsuarios=[]



ventana=Tk()
ventana.title("Pedir ingredientes al usuario")
ventana.geometry("600x600")
ventana.resizable(False,False)
ventana.config(background="gold")

combo=ttk.Combobox(ventana, state="readonly",values=["M","F"])
combo.place(x=200,y=50)

labelTexto=ttk.Label(ventana,text="Pon tus ingredientes:")
labelTexto.place(x=220,y=10)

ventana.mainloop()