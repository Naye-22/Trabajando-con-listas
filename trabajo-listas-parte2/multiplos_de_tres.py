# Múltiplos de 3 usando range con paso 3
multiplos_de_tres = list(range(3, 31, 3))

# Imprimir cada múltiplo de 3
print("Múltiplos de 3 del 3 al 30:")
for numero in multiplos_de_tres:
    print(numero)

print(f"Lista completa: {multiplos_de_tres}")
print(f"Cantidad de múltiplos: {len(multiplos_de_tres)}")