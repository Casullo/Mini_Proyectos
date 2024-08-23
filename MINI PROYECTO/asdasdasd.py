import tkinter as tk
from lista_comidas import *
ventana1 = tk.Frame()
ventana1.config(bg="green")

row=2
for menu in menus: #recorre no por indice sino por elemento
        nombre = menu.get("nombre") #toma el valor de la key
        tipo = menu.get("tipo")
        precio = menu.get("precio")
        tk.Label(ventana1,text= nombre,bg="yellow", font=("Arial", 8)).grid(row=row, column=1, pady=10)
        tk.Entry(ventana1,bg="grey").grid(row=row, column=2, padx=1)
        row+=1
        ventana1.pack(expand=1)
ventana1.mainloop()