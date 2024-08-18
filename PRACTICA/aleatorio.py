from random import *

numero entre 0 y 1
aleatorio = random()
aleatorio1 = random()
aleatorio2 = random()
aleatorio3 = random()
aleatorio4 = random()
print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)

for i in range(10):
    print(randrange(0, 100, 10))
    print(randint(0, 100))

lista = "absftrpt"
lista = ["hola", "adios", "buen dia", "buenas tardes"]

cadena_aleatoria = choice(lista)
print(cadena_aleatoria)

caracteres = "asdqwertptoyiuñlkjhcvmnx123456789!#$?"
clave = ""
for i in range(8):
    clave_aleatoria = choice(caracteres)
    clave += clave_aleatoria

print(clave)

print(dir(random))
