#script que determine si dos rectas se intersectan, son paralelas o coincidentes.
#Se solicita al usuario ingresar los valores de las pendientes y las ordenadas al origen de 2 rectas
m1 = float(input("Ingrese la pendiente de la ec1: "))
b1 = float(input("Ingrese la coordenada al origen de la ec1: "))
m2 = float(input("Ingrese la pendiente de la ec2: "))
b2 = float(input("Ingrese la coordenada al origen de la ec2: "))
# Se comparan las pendientes y las ordenadas al origen
#Si las pendientes y las ordenadas al origen son iguales, se muestra en pantalla que son coincidentes
if m1 == m2 and b1 == b2:
    print("Las rectas son coincidentes")
#Si las pendientes son iguales y las ordenadas al origen son distintas, se muestra en pantalla que son coincidentes
elif m1 == m2 and b1 != b2:
    print("Las rectas son paralelas")
#En cualquier otro caso se meustra en pantalla que se intersectan
else:
    print("Las rectas se intersectan")
