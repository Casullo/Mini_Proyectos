numeros = []

while True:
entrada = input("Ingrese un número o escriba 'fin' para terminar: ")
if entrada.lower() == "fin":
break
else:
try:
numero = int(entrada)
numeros.append(numero)
except ValueError:
print("Por favor, ingrese un número válido.")

print("Los números ingresados son:", numeros)