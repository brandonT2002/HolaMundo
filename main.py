from operaciones import operaciones
op = operaciones()
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

print(f'La suma de {num1} + {num2} es: ',op.suma(num1,num2))
print(f'La resta de {num1} - {num2} es: ',op.resta(num1,num2))