import tkinter as tk
class menusero:
    pass

ventana_comida = tk.Frame()
ventana_comida.config(bg="green")
etiqueta1 = tk.Label(ventana_comida,text= "comida 1",bg="yellow", font=("Arial", 8)).grid(row=2, column=1)
texto= tk.Entry(ventana_comida,bg="grey").grid(row=3, column=2)
etiqueta2 = tk.Label(ventana_comida,text= "comida 2",bg="yellow", font=("Arial", 8)).grid(row=3, column=1)
texto2 = tk.Entry(ventana_comida,bg="grey").grid(row=3, column=2)
etiqueta3 = tk.Label(ventana_comida,text= "comida 3",bg="yellow", font=("Arial", 8)).grid(row=4, column=1)
texto3= tk.Entry(ventana_comida,bg="grey").grid(row=3, column=2)

ventana333=menusero()

menus=[
{
    "tipo": "casero",
    "nombre":"Pasta al pesto",
    "precio":8000
},
{
    "tipo": "casero",
    "nombre":"Ensalada César",
    "precio":6500
},
{
    "tipo": "casero",
    "nombre":"Tacos al pastor",
    "precio":8500
},
{
    "tipo": "gourmet",
    "nombre":"Foie Gras a la plancha con reducción de oporto y chutney de higos",
    "precio":35000
},
{
    "tipo": "gourmet",
    "nombre":"Ossobuco a la milanesa con risotto de azafrán",
    "precio":25000
},
{
    "tipo": "gourmet",
    "nombre":"Langosta thermidor con salsa de mantequilla y brandy",
    "precio":55000
},
{
    "tipo": "vegano",
    "nombre":"Lentejas estofadas con verduras",
    "precio":7500
},
{
    "tipo": "vegano",
    "nombre":"Burrito de frijoles negros",
    "precio":6000
},
{
    "tipo": "vegano",
    "nombre":"Pasta con pesto de espinacas",
    "precio":7800
}
]
# print(menus[1].get("nombre"))


