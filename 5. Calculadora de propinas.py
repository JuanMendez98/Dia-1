propinas_propinas = [10, 15, 20]

costo_cuenta = float(input('Digita el total de la cuenta: '))

porcentaje = int(input('Digita el porcentaje de descuento: '))

if porcentaje in propinas_propinas:
    propinas = ((costo_cuenta * porcentaje)/100)
    print(f'     la propina es de{propinas: .2f}')
else:
    print('     Porcentaje de propina no valido')
    
