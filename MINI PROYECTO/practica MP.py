import tkinter as tk

ventana = tk.Tk()
ventana.title("COMILANDIA")
ventana.iconbitmap("comil.ico")
ventana.geometry("600x400")
ventana.config(bg="green")
def casera():
    ventana1 = tk.Frame()
    ventana1.config(bg="green")
    etiq1 = tk.Label(ventana1,text= "comida 1",bg="yellow", font=("Arial", 8)).grid(row=2, column=1, pady=10)
    texto1= tk.Entry(ventana1,bg="grey").grid(row=2, column=2, padx=5)
    etiq2 = tk.Label(ventana1,text= "comida 2",bg="yellow", font=("Arial", 8)).grid(row=3, column=1,pady=10)
    texto2 = tk.Entry(ventana1,bg="grey").grid(row=3, column=2, padx=5)
    etiq3 = tk.Label(ventana1,text= "comida 3",bg="yellow", font=("Arial", 8)).grid(row=4, column=1,pady=10)
    texto3= tk.Entry(ventana1,bg="grey").grid(row=4, column=2,padx=5)
    ventana1.pack()
    
def vip():
    ventana2 = tk.Frame()
    ventana2.config(bg="green")
    etiq1 = tk.Label(ventana2,text= "comida 1",bg="yellow", font=("Arial", 8)).grid(row=2, column=1)
    texto1= tk.Entry(ventana2,bg="grey").grid(row=2, column=2, padx=10)
    etiq2 = tk.Label(ventana2,text= "comida 2",bg="yellow", font=("Arial", 8)).grid(row=3, column=1)
    texto2 = tk.Entry(ventana2,bg="grey").grid(row=3, column=2, padx=10)
    etiq3 = tk.Label(ventana2,text= "comida 3",bg="yellow", font=("Arial", 8)).grid(row=4, column=1)
    texto3= tk.Entry(ventana2,bg="grey").grid(row=4, column=2, padx=10)
    ventana2.pack()
def veg():
    ventana3 = tk.Frame()
    ventana3.config(bg="green")
    etiq1 = tk.Label(ventana3,text= "comida 1",bg="yellow", font=("Arial", 8)).grid(row=2, column=1)
    texto1= tk.Entry(ventana3,bg="grey").grid(row=2, column=2)
    etiq2 = tk.Label(ventana3,text= "comida 2",bg="yellow", font=("Arial", 8)).grid(row=3, column=1)
    texto2 = tk.Entry(ventana3,bg="grey").grid(row=3, column=2)
    etiq3 = tk.Label(ventana3,text= "comida 3",bg="yellow", font=("Arial", 8)).grid(row=4, column=1)
    texto3= tk.Entry(ventana3,bg="grey").grid(row=4, column=2)
    ventana3.pack()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_comidas = tk.Menu(barra_menu)
barra_menu.add_cascade(label ='Menu Comidas', font=("Arial", 8), menu=menu_comidas)

menu_comidas.add_command(label= "Comidas Caseras", font=("Arial", 8),command=casera)
menu_comidas.add_command(label ="Comidas Gourmet", font=("Arial", 8),command=vip)
menu_comidas.add_command(label ="Comidas Vegetarianas", font=("Arial", 8),command=veg)

ventana.mainloop()




# barra menu


# etiquetas, entradas y funsion










# etiq1.place(x=0.03,y=10,width=1000,height=30)
# etiq2.place(x=10,y=50,width=1000,height=30)
# etiq3.place(x=10,y=90, width=1000, height=30)


# texto1.place(x=120,y=10, width=50,height=30)
# texto2.place(x=120,y=50,width=50,height=30)
# texto3.place(x=120,y=120, width=50)



# etiq1.pack()
# etiq2.pack()
# etiq3.pack()

# nuevo frame caseras
# framecomidas=tk.Frame(Raiz, bg="blue")
# framecomidas.config(width="400", height="300")
# texto=tk.Label(framecomidas, text="asdasdasdasdasdasd")
# check comida
# check = tk.BooleanVar()
# one=tk.Checkbutton(framecomidas, text="aca iria el diccionario comida casera de la lista comidas", variable=check)
# one.place(x=10, y=10)
# framecomidas.pack()
# one.pack()

# # boton y funcion pedido
# def pedido():
#         if one:
#             return menus[1].get("precio")
#         elif dos:
#               return menus[2].get("precio")
#         else tres:
#             return menus[3].get("precio")

# boton 
# def agregar():
    # if agregar:
    #     contador = 


# boton_pedido=tk.Button(framecomidas, text="Pedir Ya!!", command=pedido)
# ventana_casera= tk.Tk()
# ventana_casera.title("asdddd")
# ventana_casera.geometry ("600x300")
# ventana_casera.config(bg="blue")
# onevar = BooleanVar(value=True)
# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# one.grid(column=0, row=3)




