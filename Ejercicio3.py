pi = float(input("Ingrese el precio del producto: "))
des = float(input("Ingrese el porcentaje de descuento: "))

pf = pi - ((des * pi) / 100)

print("El precio final del producto, con el descuento aplicado es: ", pf)