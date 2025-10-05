#Programa que calcule el precio final de un producto después de aplicar un descuento
#Se solicita al usuario que ingrese el precio original del producto
pi = float(input("Ingrese el precio del producto: ")) 
#Se solicita al usuario el porcentaje de descuento
des = float(input("Ingrese el porcentaje de descuento: ")) 
#Se calcula el precio final aplicando el descuento
pf = pi - ((des * pi) / 100) 
#Se muestra en pantalal el precio final
print("El precio final del producto, con el descuento aplicado es: ", pf)