from tkinter import *
from tkinter import ttk
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_edad(*args):
    try:
        fecha_nacimiento = datetime.strptime(str(input_text.get()), "%d/%m/%Y")
        edad_calculada = relativedelta(datetime.now(), fecha_nacimiento)
        edad.set(f"{edad_calculada.years} aÃ±os, {edad_calculada.months} meses y {edad_calculada.days} dÃ­as")
    except ValueError:
        pass
root = Tk()
root.title("Calculando edad")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input_text = StringVar()
input_text_entry = ttk.Entry(mainframe, width=7, textvariable=input_text)
input_text_entry.grid(column=1, row=1, sticky=(W, E))

edad = StringVar()
ttk.Label(mainframe, textvariable=edad).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate_edad).grid(column=2, row=3, sticky=W)

ttk.Label(mainframe, text="fecha de nacimiento dd/mm/aaaa").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="usted tiene").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

input_text_entry.focus()
root.bind("<Return>", calculate_edad)

root.mainloop()