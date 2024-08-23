import tkinter as tk
from lista_comidas import menus
ventana = tk.Tk()
ventana.title("COMILANDIA")
ventana.iconbitmap("comil.ico")
ventana.geometry("600x400")
ventana.config(bg="black")
def solo_menu():
    ventana1 = tk.Frame()
    ventana1.config(bg="green")
    row=2
    for menu in menus: #recorre no por indice sino por elemento
        nombre = menu.get("nombre") #toma el valor de la key
        tipo = menu.get("tipo")
        precio = menu.get("precio")
        tk.Entry(ventana1,width=4,bg="grey").grid(row=row, column=2, padx=20)
        tk.Label(ventana1,text= nombre,bg="yellow", font=("Arial", 8)).grid(row=row, column=1, pady=10)
        

        row+=1

        ventana1.pack(expand=1)

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_comidas = tk.Menu(barra_menu)
barra_menu.add_cascade(label ='Menu Comidas', font=("Arial", 8), menu=menu_comidas)

menu_comidas.add_command(label= "Seleccionar Menues", font=("Arial", 8),command=solo_menu)


ventana.mainloop()




