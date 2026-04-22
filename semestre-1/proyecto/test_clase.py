from controller import modificar_celda, operar_celda
def matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

tabla = matriz(10, 10)

while True:
    for fila in tabla:
        print(fila)

    opcion = input("\nEscriba 'modificar' para cambiar una celda, 'operar' para sumar/restar, o 'salir': ")

    if opcion.lower() == 'salir':
        break

    # --- MODIFICAR UNA CELDA ---
    if opcion.lower() == 'modificar':
        modificar_celda(tabla)

    # --- OPERAR ENTRE DOS CELDAS ---
    elif opcion.lower() == 'operar':
        operar_celda(tabla)