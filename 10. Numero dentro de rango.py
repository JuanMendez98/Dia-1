while True:

    try:
        numero = float(input("Ingresa un numero: "))

        if 1 <= numero <= 10:
            print("     El numero esta dentro del rango de 1 a 10")
        else:
            print("     El numero no esta dentro del rango de 1 a 10")
    except:
        print('         No se permiten letras y/o caracteres, solo numeros')