# Encontar el menor y el mayor y mostar su posicion
filas_numeros = []
columnas_numeros = []
posicion_menor = [0,0]
posicion_mayor = [0,0]
mayor=0
menor=0

for i in range(3):    
    for j in range(3):
        numero = int(input("Ingrese un número: "))
        columnas_numeros.append(numero)
    filas_numeros.append(columnas_numeros)
    columnas_numeros = []
    
for i in range(len(filas_numeros)):
    for j in range(len(filas_numeros[i])):
        
        if (filas_numeros[i][j] > mayor):
            mayor = filas_numeros[i][j]
            posicion_mayor[0]=j
            posicion_mayor[1]=i

        if menor == 0:       
            menor = filas_numeros[i][j]
            posicion_menor[0]=j
            posicion_menor[1]=i
            
        if (filas_numeros[i][j] < menor):
            menor = filas_numeros[i][j]  
            posicion_menor[0]=j
            posicion_menor[1]=i
            
print(f"El numero mayor es {mayor} y su pocicion es {posicion_mayor}")
print(f"El numero mayor es {menor} y su pocicion es {posicion_menor}")     
     