#en este solo codigo se resuelven los ejercicios 6 y 7
#con la linea de codigo que posee el "if" se resuelve el ejercicio 7
#quitando esa linea queda resuelto el ejercicio 6

import time
i = 0
while i < 100 :
    i += 1
    time.sleep(0.05)
    if i % 2 == 0: #quitar esta linea de codigo para ejercicio 6, agregar para ejercicio 7.
        print("Cargando... ",i,end='\r')
else:
    time.sleep(1)
    print("Fin del programa")