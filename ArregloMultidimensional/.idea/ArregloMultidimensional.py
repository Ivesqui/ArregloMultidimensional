# Programa: Búsqueda en Arreglo Multidimensional (versión mejorada)

# Creamos una matriz 3x3 con valores repetidos
matriz = [
    [10, 20, 30],
    [20, 50, 20],
    [70, 80, 20]
]

# Función para buscar todas las ocurrencias de un valor en la matriz
def buscar_todos(matriz, valor):
    posiciones = []
    for i in range(len(matriz)):          # Filas
        for j in range(len(matriz[i])):   # Columnas
            if matriz[i][j] == valor:
                posiciones.append((i, j))
    return posiciones

# Mostramos la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Pedimos al usuario el valor a buscar
valor_buscado = int(input("Ingresa el valor que deseas buscar: "))

# Buscamos el valor en la matriz
posiciones = buscar_todos(matriz, valor_buscado)

# Mostramos el resultado
if posiciones:
    print(f"✅ El valor {valor_buscado} se encontró en las posiciones:")
    for pos in posiciones:
        print(f"  → Fila {pos[0]}, Columna {pos[1]}")
else:
    print(f"❌ El valor {valor_buscado} no se encontró en la matriz.")
