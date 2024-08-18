import tkinter as tk
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('900x600')
# se abre menu de la ventana
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
# se abre 2 cascada dentro de la barra menu
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label ='Principal', menu=menu_principal)
barra_menu.add_cascade(label ='princpal2',menu=menu_principal)

# se crea un submenu dentro del menu principal
submenu = tk.Menu(menu_principal)
# se crea una cascada dentro de ese menu
menu_principal.add_cascade(label ='Opciones', menu=submenu)
# se crean en el submenu las 2 opciones
submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Opción 2')

ventana.mainloop()