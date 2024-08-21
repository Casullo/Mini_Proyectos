# |class SeleccionEntrega:
#     """
#     Gestionar la selección de la forma de entrega del pedido.
#     """
    
#     def __init__(self, numero_pedido):
#         self.numero_pedido = numero_pedido

#     def seleccionar_entrega(self):
#         """
#         Función que presenta las opciones de entrega al usuario y devuelve la selección.

#         Returns:
#             str: 'domicilio' si el usuario elige envío a domicilio, 'retiro' si elige retiro en el local.
#         """

#         while True:
#             print("Selecciona como queres recibir tu pedido:")
#             print("1. Te mandamos a domicilio")
#             print("2. Retiras del local")
#             opcion = input("Elegí tu opción preferida: ")

#             if opcion == '1':
#                 # Solicitar la dirección de envío
#                 direccion = input("Dirección donde enviamos: ")
#                 print(f"¡Tu pédido {self.numero_pedido} esta confirmado! Te lo mandamos a : {direccion}")
#                 return 'domicilio'
#             elif opcion == '2':
#                 print(f"¡Tu pedido {self.numero_pedido} te espera en el local, podes pasar a retirarlo desde las XX") #XX reemplazar por el metodo o funcion que a la hora actual le sume el tiempo de coccion y entregue al usuario un horario estimado
#                 return 'retiro'
#             else:
#                 print("Opción inválida. Por favor, ingrese 1 o 2.")

# prueba = SeleccionEntrega()
# print(prueba)
import tkinter as tk
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu, bg="blue")
# def abrir_ventana2():
#     global ventana2
#     ventana2 = tk.Tk()
#     ventana2.title("Tipo de envio")
#     ventana2.geometry('600x200')
def abrir_ventana2():
    ventana2 = tk.Frame(ventana)
    ventana2.config(width="400", height="200")
    ventana2.pack()
#se crean los botones principales de la barra de menu
menu_principal = tk.Menu(barra_menu)
menu_principal2 = tk.Menu(barra_menu)
#Se le asigna la etiqueta a cada boton principal
barra_menu.add_cascade(label ='Principal', menu=menu_principal)
barra_menu.add_cascade(label ='Principal2', menu=menu_principal2)
#Se crean los submenu del menu principal
submenu = tk.Menu(menu_principal)
submenu2 = tk.Menu(menu_principal2)
#Se le asigna la etiqueta al submenu
menu_principal.add_cascade(label ='Opciones', menu=submenu)
submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Opción 2')
#Se le asigna la etiqueta al submenu2
menu_principal2.add_cascade(label ='Ver', menu=submenu2)
submenu2.add_command(label = 'Claro')
submenu2.add_command(label = 'Oscuro', command=abrir_ventana2)

ventana.mainloop()