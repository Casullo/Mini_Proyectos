lista_numeros= []

while True:
numero = input("Ingrese un número o 'fin' para terminar: ")
if numero == 'fin':
break
lista_numeros.append(int(numero))

# lista_numeros.sort()
# lista_ordenada=sorted(lista_numeros)

#ordenamiento burbuja
for numPasada in range(len(lista_numeros)-1,0,-1):
for i in range(numPasada):
print(i)
if lista_numeros[i]>lista_numeros[i+1]:
temp = lista_numeros[i]
lista_numeros[i] = lista_numeros[i+1]
lista_numeros[i+1] = temp

print(lista_numeros)