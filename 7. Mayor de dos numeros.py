while True:
    
    try:
        numero1 = float(input("Ingresa el primer numero: "))
        numero2 = float(input("Ingresa el segundo numero: "))
        
        if numero1 > numero2:
            print(f"     El numero mayor es: {numero1}")
        elif numero2 > numero1:
            print(f"     El numero mayor es: {numero2}")
        else:
            print("     Los dos numeros son iguales")

    except:
        print("         Ingresa numeros validos")
