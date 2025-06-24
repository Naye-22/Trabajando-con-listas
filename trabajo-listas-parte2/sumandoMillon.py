# Creando una lista de 1 hasta 1 millon
numeros = list(range(1, 1_000_001))

# Verifica el mínimo y el máximo
print("Valr minimo:", min(numeros))
print("Valor maximo:", max(numeros))
print("=" * 30)

# Sumatoria de los numeros de la listaa
print("Sumatoria:", sum(numeros)) # debe darnos 500000500000
print("=" * 60)
print("Los primeros 10 números:", numeros[:10])
print("Los ultimos 10 números:", numeros[-10:])
print(f"Tamaño de la lista: {len(numeros):,} números")
