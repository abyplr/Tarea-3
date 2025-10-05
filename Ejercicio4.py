#Conversión de coordenadas y localización geográfica.
#Coordenada 1 (Estatua de la Libertad)
latg1 = 40
latm1 = 41 /60
lats1 = 21 / 3600
long1 = 74
lonm1 = 2 / 60
lons1 = 40 / 3600
#Coordenada 2 (Torre Eiffel)
latg2 = 48
latm2 = 51 / 60
lats2 = 12 / 3600
long2 = 2
lonm2 = 20 / 60
lons2 = 55 / 3600
#Coordenada 3 (Taj Mahal)
latg3 = 34
latm3 = 3 / 60
lats3 = 8 / 3600
long3 = 151
lonm3 = 12 / 60
lons3 = 33 / 3600
#Conversión de coordenadas a decimal
declat1 = latg1 + latm1 + lats1
declon1 = - (long1 + lonm1 + lons1)
declat2 = latg2 + latm2 + lats2
declon2 = long2 + lonm2 + lons2
declat3 = - (latg3 + latm3 + lats3)
declon3 = long3 + lonm3 + lons3
#Se muestran al usuario las coordenadas en decimales y la ubicación 
print("Coordenadas de la Estatua de la Libertad:")
print("Lat = ", round(declat1, 3))
print("Long = ", round(declon1, 3))
print("Coordenadas de la Torre Eiffel:")
print("Lat = ", round(declat2, 3))
print("Long = ", round(declon2, 3))
print("Coordenadas del Taj Mahal:")
print("Lat = ", round(declat3, 3))
print("Long = ", round(declon3, 3))