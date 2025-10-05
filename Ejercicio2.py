#Programa que solicite al usuario dos números y realice las operaciones básicas
#Se solicita al usuario que ingrese dos números
num1 = float (input("Ingrese el primer número: "))
num2 = float (input("Ingrese el segundo número: "))
#Operaciones básicas
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
pot = num1 ** num2
rc1 = num1 ** (1/2)
rc2 = num2 ** (1/2)
#Se muestran los resultados al usuario
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", mult)
print("División: ", div)
print("Potencia: ", pot)
print("Raiz cuadrada del primer número: ", rc1)
print("Raiz cuadrada del segundo número: ", rc2)