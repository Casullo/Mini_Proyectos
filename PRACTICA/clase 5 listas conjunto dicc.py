conjunto_a = {"a", "b", "c"}
conjunto_b = set()
conjunto_c = {"c", "d"}

# aplicar interseccion, diferencia y Union entre conjunto_a y conjunto_c
# aplicar union entre conjunto_a y conjunto b

#interseccion (deja solo el dato que se repite)
print(conjunto_a & conjunto_c)
#diferencia (devuelve los elementos que no se repiten en el c y devuelve solo los del conjunto a)
print(conjunto_a - conjunto_c)
#union
print(conjunto_a | conjunto_c)