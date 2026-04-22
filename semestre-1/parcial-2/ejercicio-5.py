# sacar el promedio por filas y guardarlo en un arreglos
# [6, 15, 24]
filas_numeros = []
columnas_numeros = []
sumas = []
suma = 0
# Insertando numeros manualmente a la matriz
for i in range(3):    
    for j in range(3):
        numero = int(input("Ingrese un número: "))
        columnas_numeros.append(numero)
    filas_numeros.append(columnas_numeros)
    columnas_numeros = []
    
for fila in filas_numeros:
    print(f"fila [{filas_numeros.index(fila)}]")
    print(fila)

for i in range(len(filas_numeros)):
    for j in range(len(filas_numeros[i])):
        suma = suma + filas_numeros[i][j]
    sumas.append(suma)
    suma=0
    
print(sumas)