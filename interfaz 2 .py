from tkinter import *
from tkinter import ttk
from tkinter import messagebox


usuario=""
contraseña=""
confirmar=""
vUsuarios=[]

def guardardatos():
    usuario=entryusuario.get()
    contraseña=entrycontraseña.get()
    confirmar=entryconfirmar.get()
    if contraseña==confirmar:
        vUsuarios.append(usuario)
        vUsuarios.append(contraseña)
        print(vUsuarios)
    messagebox.showinfo("Usuario Guardado",f"Usuario guaraddo")   
    







ventana=Tk()
ventana.title("Pedir datos al usuario")
ventana.geometry("500x500")
ventana.resizable(False,False)
ventana.config(background="gold")

labelTexto=ttk.Label(ventana,text="Pon tus datos:")


labelusuario=ttk.Label(ventana,text="Introduce tu usuario")
entryusuario=ttk.Entry(ventana)
labelcontraseña=ttk.Label(ventana,text="Intruce tu contraseña")
entrycontraseña=ttk.Entry(ventana,show="*")

botonguardar=ttk.Button(ventana,text="Guardar",command=guardardatos)
botonsalir=ttk.Button(ventana,text="Salir",command=ventana.destroy)


labelTexto.grid(row=0,column=1)
labelusuario.grid(row=1,column=0)
entryusuario.grid(row=1,column=1,padx=10,pady=10)

labelcontraseña.grid(row=3,column=0)
entrycontraseña.grid(row=3,column=1,padx=10)

labelconfirmar=ttk.Label(ventana,text="Repite la contraseña")
entryconfirmar=ttk.Entry(ventana,show="*")

labelconfirmar.grid(row=5,column=0,padx=10,pady=10)
entryconfirmar.grid(row=5,column=1)


botonguardar.grid(row=6,column=1)
botonsalir.grid(row=6,column=0)
ventana.mainloop()