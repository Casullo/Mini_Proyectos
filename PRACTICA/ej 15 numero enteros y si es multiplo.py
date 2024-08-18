def es_multiplo(a,b):
    if a % b == 0:
        x = True
    else:
        x = False
    return x
primer_valor= int(input("ingrese el primer numero "))
segundo_valor= int(input("ingrese el segundo numero "))
resultado = es_multiplo(primer_valor,segundo_valor)
print("es multiplo" if resultado  else "no es multiplo")