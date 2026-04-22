# Contar los numeros pares e impares de la matriz
filas_numeros = []
columnas_numeros = []

cant_impares = 0
cant_pares = 0


for i in range(3):    
    for j in range(3):
        numero = int(input("Ingrese un número: "))
        columnas_numeros.append(numero)
    filas_numeros.append(columnas_numeros)
    columnas_numeros = []

for i in range(len(filas_numeros)):
    for j in range(len(filas_numeros[i])):
        if((filas_numeros[i][j] % 2 )== 0):
            print("Par")
            cant_pares =  cant_pares + 1
        else:
            cant_impares =  cant_impares + 1
            print("Impar")
            
print("Cantidad de pares", cant_pares)
print("Cantidad de impares", cant_impares)            
            
                         
    