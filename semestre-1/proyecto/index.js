
// def crear_matriz_vacia(filas, columnas):
//     matriz = []
//     for i in range(filas):
//         fila = []
//         for j in range(columnas):
//             fila.append(0)
//         matriz.append(fila)
//     return matriz

// tabla = crear_matriz_vacia(10, 10)

// for fila in tabla:
//     print(fila)

// celda = input("Ingrese la celda a modificar (formato: fila,columna): ")

// print(map(int, celda.split(",")))

var posicion = '0o0';

_posicion = posicion.split("o").map(Number);

console.log( _posicion );