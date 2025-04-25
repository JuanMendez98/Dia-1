while True:
    try:
        edad = int(input("Cual es tu edad? "))

        if edad >= 18:
            print("     Eres mayor de edad")
        else:
            print("     Eres menor de edad")
    except:
        print("     Ingresa numero valido para edad")


