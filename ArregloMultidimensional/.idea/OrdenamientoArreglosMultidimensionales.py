# Programa: Ordenar fila específica con QuickSort

# Matriz 3x3
matriz = [
    [5, 9, 1],
    [20, 15, 10],
    [8, 7, 6]
]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        matriz[fila] = quicksort(matriz[fila])
    else:
        print("Fila inválida")

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 2 (tercera fila)
ordenar_fila(matriz, 2)

# Mostrar matriz modificada
print("\nMatriz con la fila 2 ordenada (QuickSort):")
for fila in matriz:
    print(fila)
