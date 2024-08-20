
import tkinter as tk
# from lista comidas import *
# main frame



Raiz = tk.Tk()
Raiz.title('COMILANDIA')
Raiz.iconbitmap("comil.ico")
Raiz.geometry('600x600')
Raiz.resizable(1,1)
Raiz.config(bg="green")
# barra menu
barra_menu = tk.Menu(Raiz)
Raiz.config(menu=barra_menu)
# tres menu en cascada de comidas
menu_comidas = tk.Menu(barra_menu)
barra_menu.add_cascade(label ='Menu Comidas', menu=menu_comidas)
menu_comidas.add_cascade(label= 'Comidas Caseras')
menu_comidas.add_cascade(label ='Comidas Gourmet')
menu_comidas.add_cascade(label ='Comidas Vegetarianas')

# etiquetas, entradas y funsion
etiq1 = tk.Label(Raiz,text= "comida 1",bg="yellow")
etiq2 = tk.Label(Raiz,text= "comida 2",bg="yellow")
etiq3 = tk.Label(Raiz,text= "comida 3",bg="yellow")


texto1= tk.Entry(Raiz,bg="grey")
texto2 = tk.Entry(Raiz,bg="grey")
texto3= tk.Entry(Raiz,bg="grey")




# etiq1.place(x=0.03,y=10,width=1000,height=30)
# etiq2.place(x=10,y=50,width=1000,height=30)
# etiq3.place(x=10,y=90, width=1000, height=30)


texto1.place(x=120,y=10, width=50,height=30)
texto2.place(x=120,y=50,width=50,height=30)
texto3.place(x=120,y=120, width=50)






etiq1.pack(pady=6)
etiq2.pack(pady=6)
etiq3.pack(pady=6)
texto1.pack(pady=6)
texto2.pack(pady=6)
texto3.pack(pady=6)
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


Raiz.mainloop()

