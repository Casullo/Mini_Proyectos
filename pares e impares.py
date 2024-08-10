

pares = 0
impares = 0

for i in range (10):
    #ingreso de datos (entrada)
    numero_ingresado = int(input("introducir un numero: "))

    # estudio si es par o inpar (condicional)
    if numero_ingresado % 2 == 0:
        pares = pares +1
    else:
        impares = impares +1
#salida de datos (resultados)
print ("la cantidad de numeros pares es:", pares )
print ("la cantidad de numeros impares es:", impares )