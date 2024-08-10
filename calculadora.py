while True:
    try:
        numero_1 = int(input("ingrese el primer numero "))
        numero_2 = int(input("ingrese el segundo numero "))   
        suma = (numero_1 + numero_2);
        resta = (numero_1 - numero_2);
        multi = (numero_1 * numero_2);
        division = (numero_1 / numero_2);
        print (" la suma de los numeros es: ," , suma)
        print (" la resta de los numeros es: ," , resta)
        print (" la multiplicación de los numeros es: ," , multi)
        print  (" la división de los numeros es: ," , division)
    except ValueError:
        print (" los numeros ingresados son incorrectos")    
    continue
    
    