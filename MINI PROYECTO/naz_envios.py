class SeleccionEntrega:
    """
    Gestionar la selección de la forma de entrega del pedido.
    """
    
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido

    def seleccionar_entrega(self):
        """
        Función que presenta las opciones de entrega al usuario y devuelve la selección.

        Returns:
            str: 'domicilio' si el usuario elige envío a domicilio, 'retiro' si elige retiro en el local.
        """

        while True:
            print("Selecciona como queres recibir tu pedido:")
            print("1. Te mandamos a domicilio")
            print("2. Retiras del local")
            opcion = input("Elegí tu opción preferida: ")

            if opcion == '1':
                # Solicitar la dirección de envío
                direccion = input("Dirección donde enviamos: ")
                print(f"¡Tu pédido {self.numero_pedido} esta confirmado! Te lo mandamos a : {direccion}")
                return 'domicilio'
            elif opcion == '2':
                print(f"¡Tu pedido {self.numero_pedido} te espera en el local, podes pasar a retirarlo desde las XX") #XX reemplazar por el metodo o funcion que a la hora actual le sume el tiempo de coccion y entregue al usuario un horario estimado
                return 'retiro'
            else:
                print("Opción inválida. Por favor, ingrese 1 o 2.")

# prueba = SeleccionEntrega()
# print(prueba)