import tkinter as tk

# print(dir(tk))

# ingrear un nombre y saludarlo


def mostrar_saludo():
    nombre = entrada.get()
    saludo = f"Hola, {nombre}"
    etiquete_saludo.config(text=saludo)


ventana = tk.Tk()
ventana.geometry("600x600")
ventana.title("Mi primera GUI")
# ventana.iconbitmap() .ico

# entrada de datos "input"
entrada = tk.Entry(ventana)
entrada.pack(side="top", pady="10")

# boton de enviar input
boton = tk.Button(ventana, text="Mostrar saludo", command=mostrar_saludo)
boton.pack(pady="10")


# etiqueta para mostrar el saludo en la ventana raiz
etiquete_saludo = tk.Label(ventana, text="")
etiquete_saludo.pack(side="left")

ventana.mainloop()
