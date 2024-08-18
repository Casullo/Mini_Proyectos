# edad = int(input("ingrese su edad"))
# edad_a =18
# if edad >= edad_a:
#     print ("usted es mayor")
# elif edad < edad_a:
#     print ("ustedes es menor")

import tkinter

def edad():
    x = int(entrada.get())
    if x < 18:
        mensaje = f" maldito menor"
        etiqueta_edad.config(text=mensaje)
    else:
        mensaje2 = f" maldito old"
        etiqueta_edad.config(text=mensaje2)


ventana= tkinter.Tk()
ventana.title("Calculadora malefica de años")
ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana, text = "carga tu edad ahi dale que te haces mas viejo -->", font=("Arial", 10))
etiqueta.pack()
# input
entrada = tkinter.Entry(ventana)
entrada.pack(side="top", pady="10")
# boton
boton = tkinter.Button(ventana, text="cargar", command=edad)
boton.pack(pady="10")

etiqueta_edad = tkinter.Label(ventana, text="")
etiqueta_edad.pack(side="right")         
ventana.mainloop()
