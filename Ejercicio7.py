a = int(input('Ingrese la longitud del lado a: '))
b = int(input('Ingrese la longitud del lado b: '))
c = int(input('Ingrese la longitud del lado c: '))

if a + b > c and b + c > a and a + c> b:
    print(" ")
    if a == b == c:
        print("Es un triángulo equilátero")
    elif a == b != c or b == c != a or a == c != b:
        print("Es un triángulo isósceles")
    else:
        print("Es un trángulo escaleno")
else:
    print("Los lados no forman un tríangulo. Ingrese nuevos valores")