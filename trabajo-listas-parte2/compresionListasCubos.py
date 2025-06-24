# Usando comprensión de listas para crear la lista de cubos
print("Cubos con comprensión de listas:")
cubos = [numero ** 3 for numero in range(1, 11)]
for cubo in cubos:
    print(cubo)