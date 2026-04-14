# Crear un arreglo 
# Crear 10 numeros ingresados manualmente
# Imprimir los numeros del arr eglo
# Sumar y mostar el promedio

numeros = []
suma = 0

for i in range(10):
    numero_nuevo = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero_nuevo)
    
for i in range(len(numeros)):
    suma +=numeros[i]
    
promedio = suma/len(numeros)            
print(promedio)    
print(numeros)    


# Dado un arreglo, recórrelo usando while y muestra todos sus elementos.
nombres=["nombre-1", "nombre-2","nombre-3", "nombre-4", "nombre-5"] # tiene 4 nombres
contador = 0 # inicia desde 0
                # 4
print("Impimir la longitud", len(nombres))  
print("❤️ Contador antes de entrar al while",contador)              
while contador < len(nombres):
    
    print("🚀contador al inicio del while",contador)   
    print(nombres[contador])
    contador +=1 # 1, 2, 3
    print("💕contador al final del while",contador)   