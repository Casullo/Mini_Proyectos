# Determinar cuantos nros se desea ingresar
cant=int(input('Cuantos nros desea ingresar? '))
lista=[]
for i in range(0,cant):
    lista.append(int(input('Ingrese valor: ')))

for i_pasada in range(len(lista)-1,0,-1):
    for i in range(i_pasada):
        if lista[i]>lista[i+1]:
            temp=lista[i]
            lista[i]= lista[i+1]
            lista[i+1] = temp

print (lista)

# print(lista)
#lista.sort()
# print(lista)
#sorted(lista)
#print(lista)