#Convertir dólares americanos a pesos mexicanos, euros, libras esterlinas, yuanes y rublos
#Tasas de cambio fijas
MXN = 18.44
EUR = 0.85
GBP = 0.74
CNH = 7.13
RUB = 82.55
#Se muestran las tasas de cambio fijas al usuario
print("Tasas de cambio fijas:")
print("1 USD = ", MXN, "MXN") 
print("1 USD = ", EUR, "EUR")
print("1 USD = ", GBP, "GBP")
print("1 USD = ", CNH, "CNH")
print("1 USD = ", RUB, "RUB")
#Se solicita al usuario ingresar la cantidad de dólares
USD = float (input ("Ingrese la cantidad de dólares a convertir: "))
#Se muestra al usuario la conversión
print(USD, "USD = ", (USD * MXN), "MXN")
print(USD, "USD = ", (USD * EUR), "EUR")
print(USD, "USD = ", (USD * GBP), "GBP")
print(USD, "USD = ", (USD * CNH), "CNH")
print(USD, "USD = ", (USD * RUB), "RUB")

