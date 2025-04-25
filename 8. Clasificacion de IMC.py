while True:
    try:
        peso = float(input("Ingresa peso en kg: "))
        
        altura = float(input("Ingresa altura en metros: "))
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            print("     Bajo peso")
        elif 18.5 <= imc < 24.9:
            print("     Normal")
        elif 25 <= imc < 29.9:
            print("     Sobrepeso")
        else:
            print("     Obesidad")

    except:
        print("     Ingresa un valor valido para el peso y la altura")
