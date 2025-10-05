m1 = float(input("Ingrese la pendiente de la ec1: "))
b1 = float(input("Ingrese la coordenada al origen de la ec1: "))
m2 = float(input("Ingrese la pendiente de la ec2: "))
b2 = float(input("Ingrese la coordenada al origen de la ec2: "))

if m1 == m2 and b1 == b2:
    print("Las rectas son coincidentes")
elif m1 == m2 and b1 != b2:
    print("Las rectas son paralelas")
else:
    print("Las rectas se intersectan")
