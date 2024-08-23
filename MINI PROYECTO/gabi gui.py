
class BebidasMenu:

    def __init__(self, bebida, precio, ingredientes):
        self.bebida = bebida
        self.precio = precio
        self.ingredientes = ingredientes

    def mostrar_bebida(self):
        print (f' {self.bebida}: {self.precio}\n Ingredientes: {self.ingredientes}')

campari = BebidasMenu('Campari', 3500, 'Naranja, aguardiente y jarabe azucarado')
# campari.mostrar_bebida()

class BebidasSinAlcohol (BebidasMenu):

 limonada = BebidasMenu('Limonada', 2000, 'Limón, azucar, agua')

 limonada.mostrar_bebida()
