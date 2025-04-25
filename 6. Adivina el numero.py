
numero_secreto = 7

while True:
    try:
        numero_usuario = int(input("Adivina el numero secreto en un rango entre 0 y 9: "))
        
        if numero_usuario > numero_secreto:
            print("         El numero es mayor que el numero secreto")
        elif numero_usuario < numero_secreto:
            print("         El numero es menor que el numero secreto")
        else:
            print("         Adivinaste el numero secreto")
            
    except:
        print("         Ingresa un numero valido")