#Programa que pida un número entero y determine si es par o impar 
#Se solicita al usuario ingresar un número
num = int(input("Ingrese un número entero: "))
#Se calcula el residuo al dividir entre 2
num2 = num % 2
#Si el residuo es 0, se muestra en pantalla que el número es par
if num2 == 0:
    print("Es par")
#Si el residuo es 1, se muestra en pantalla que el número es impar
elif num2 == 1:
    print("Es impar")
#En cualquier otro caso se muestra en pantalla que es un entero no válido
else:
    print("Entero no válido")
    