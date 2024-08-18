diccionario = {}
texto = input("ingresar texto :")
#los strings son iterables como lista diccionarios
for i in texto:
    if i in diccionario:
        diccionario[i] = +1
    else:
        diccionario[i] = 1
print (diccionario)
