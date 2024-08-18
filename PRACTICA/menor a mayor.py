# Ejercicio de menor a mayor
n=int(input('Ingrese un número: '))
n1=int(input('Ingrese el segundo número: '))
n2=int(input('Ingrese tercer número: '))

if n > n1 and n > n2:
    if n1 > n2:
        print(n2,' ', n1,' ', n )
    else:
        print(n1, ' ',n2, ' ', n)

elif n1 > n and n1 > n2:
    if n > n2:
        print(n2,' ', n,' ', n1)
    else:
        print(n, ' ',n2, ' ', n1)

else:
    if n1 > n:
        print(n,' ', n1,' ', n2)
    else:
        print(n1, ' ',n, ' ', n2)