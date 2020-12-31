from tkinter import *
from tkinter import messagebox



palabra="Hola".upper()       #Cambiar por la palabra para adivinar
VidasPantalla=5
tusletras=[]
ListaPalabra=[]
ListaCasillas=[]
aciertos=0

for i in palabra:                                                                                   
    ListaPalabra.append(i)               
    ListaCasillas.append("_")


def Probar():
    global VidasPantalla
    global aciertos
   
    letra=Letra.get().upper() 

    if letra in palabra:

        if letra in tusletras:
            VidasPantalla=VidasPantalla-1
            vidas_pantalla.config(text=f"Vidas: {VidasPantalla}")

        else:
            tusletras.append(letra)
            indice=0
            for i in ListaPalabra:
                if i ==letra:
                    ListaCasillas[indice]=letra
                    aciertos=aciertos+1
                indice=indice + 1
        
    else: 
        VidasPantalla=VidasPantalla-1
        vidas_pantalla.config(text=f"Vidas: {VidasPantalla}")
        
    
    pantalla.config(text=ListaCasillas)
    if aciertos==len(palabra):
        messagebox.showinfo(title="Palabra", message="GANASTE")
        root.destroy()
    if VidasPantalla==0:
        messagebox.showinfo(title="Palabra", message=f"Perdiste la palabra es {palabra}")
        root.destroy()

    Letra.set("")

def CJ():
    messagebox.showinfo(title="Palabra", message="Inroduce ¡solo una letra! que creas que forma parte de la palabra oculta")

def limitador():
    if len(Letra.get()) > 0:
        Letra.set(Letra.get()[0])


root=Tk()
root.title("Palabra")
root.resizable(0, 0)



frame_1=Frame(root)
frame_1.pack()

menu=Menu(root)
root.config(menu=menu)

AyudaMenu=Menu(menu, tearoff=0)
AyudaMenu.add_command(label="¿Como Jugar?", command=CJ)

menu.add_cascade(label="Ayuda",menu=AyudaMenu)

pantalla=Label(frame_1, text=ListaCasillas)
pantalla.config( fg="black",font=("Verdana",100))
pantalla.pack(anchor=CENTER)

vidas_pantalla=Label(frame_1, text=f"Vidas: {VidasPantalla}")
vidas_pantalla.config(fg="black",font=("Verdana",50) )
vidas_pantalla.pack()

frame_2=Frame(root)
frame_2.pack()

Letra=StringVar()
Letra_entry=Entry(frame_2, textvariable=Letra)
Letra.trace("w", lambda *args: limitador())
Letra_entry.config( fg="black",font=("Verdana",50), justify="center",width=10)
Letra_entry.grid(column=0, row=0, padx=10, pady=10)


Accion=Button(frame_2,text="Ingresar Letra", command=Probar)
Accion.config(height=5,width=20, bg="#0A97CB")
Accion.grid(column=1, row=0, padx=10, pady=10)

                                      

root.mainloop()