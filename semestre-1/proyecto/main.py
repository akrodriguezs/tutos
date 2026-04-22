from model.cell_modell import Celda

contador = 0

def crear_matriz_vacia(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(Celda())
        matriz.append(fila)
    return matriz

tabla = crear_matriz_vacia(10, 10)

while True:
    # Mostrar la tabla sin corchetes externos
    for fila in tabla:
        print(fila)

    posicion = input("Ingrese la celda a modificar (formato: fila,columna): ")
    if posicion == "salir":
        break
    
    fila, columna = map(int, posicion.split(","))
    
    valor = input("Ingrese el valor de la celda: ")
    tipo = input("Ingrese el tipo: ")
    
    # Crear una nueva celda con los valores ingresados
    tabla[fila][columna] = Celda(
        numero=int(numero),
        tipo=tipo,
        forma=forma
    )