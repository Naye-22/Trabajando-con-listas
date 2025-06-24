# Crear una lista de los primeros 10 cubos (del 1 al 10)
cubos = []

for numero in range(1, 11):
    cubo = numero ** 3
    cubos.append(cubo)

# Imprimir cada cubo
for cubo in cubos:
    print(cubo)