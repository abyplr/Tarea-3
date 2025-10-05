#Tipo de triángulo
#Se piden al usuario ingresar la longitud de los tres lados del triángulo
a = int(input('Ingrese la longitud del lado a: '))
b = int(input('Ingrese la longitud del lado b: '))
c = int(input('Ingrese la longitud del lado c: '))
#Se verifica si las longitudes pueden formar un triángulo
if a + b > c and b + c > a and a + c> b:
    print(" ")
    #Si los tres lados son iguales, se muestra en pantalla que es un triángulo equilátero
    if a == b == c:
        print("Es un triángulo equilátero")
    #Si solo dos lados son iguales, se muestra en pantalla que es un triángulo isósceles
    if a == b != c or b == c != a or a == c != b:
        print("Es un triángulo isósceles")
    #Si los tres lados son diferentes, se muestra en pantalal que es un triángulo escaleno
    if a != b != c:
        print("Es un trángulo escaleno")
#Si no se cumple la desigualdad triangular, se muestra un mensaje de error
else:
    print("Los lados no forman un tríangulo. Ingrese nuevos valores")