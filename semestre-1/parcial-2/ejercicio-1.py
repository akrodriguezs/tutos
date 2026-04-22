filas_numeros = []
columnas_numeros = []
contador = 0
suma = 0
# Insertando numeros manualmente a la matriz
for i in range(3):    
    for j in range(3):
        numero = int(input("Ingrese un número: "))
        columnas_numeros.append(numero)
    filas_numeros.append(columnas_numeros)
    columnas_numeros = []
    
# while contador < len(filas_numeros):
#     print(filas_numeros[contador])
#     contador += 1  
    
# for i in range(len(filas_numeros)):
#     print(f"fila [{i}]")
#     print (filas_numeros[i])    
    
for fila in filas_numeros:
    print(f"fila [{filas_numeros.index(fila)}]")
    print(fila)
    
    
for i in range(len(filas_numeros)):
    for j in range(len(filas_numeros[i])):
        suma = suma + filas_numeros[i][j]
        
print(f"La suma de los números es: {suma}")   
# PROMEDIO GENRAL
print(f"El promedio de los números es: {suma/len(filas_numeros)}")     
       
    
     