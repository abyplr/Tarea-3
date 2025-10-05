#Programa que solicite al usuario un año y que indique si es bisiesto o no
#Se solicita al usuario ingresar un año
año = int(input("Ingrese un año: "))
# Se calculan los residuos de dividir el año entre 4, 100 y 400
añob = año % 4
año100 = año % 100
año400 = año % 400
#Si muestra cualquiera de las 2 condiciones (divisible entre 4 y no entre 100, o divisible entre 400), se muestra en pantalla que es año bisiesto
if (añob == 0 and año100 != 0) or (añob == 0 and año100 == 0 and año400 == 0):
    print("Es año bisiesto")
#En cualquier otro caso se muestra en pantalla que no es año bisiesto
else:
    print("No es año bisiesto")