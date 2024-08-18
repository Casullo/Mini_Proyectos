#cantidad_caracteres = len("astronomico")
#print (cantidad_caracteres)

# texto = input("introducir su texto: ")

# cantidad_caracteres = 0

# for i in texto:
#     if i != " ": 
#         cantidad_caracteres = cantidad_caracteres + 1

# print("la cantidad de caracteres es", cantidad_caracteres)


def conta_caras():
    texto = str(input("hola madafaka mete nomas tu texto aca"))
    cantidad = 0
    for c in texto:
        if c != " ":
            cantidad += 1
    print("la cantidad weonea es, ", cantidad)
conta_caras()
