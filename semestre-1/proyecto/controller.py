def modificar_celda(tabla):
    posicion = input("Ingrese la posición a modificar (fila,columna): ")
    fila, columna = map(int, posicion.split(','))
    print(f"Valor actual en ({fila},{columna}): {tabla[fila][columna]}")
    tabla[fila][columna] = input("Ingrese el nuevo valor: ")
    
def operar_celda(tabla):
    posicion = input("Ingrese la celda donde se va a guardar el resultado (fila,columna): ")
    fila, columna = map(int, posicion.split(','))
    pos1 = input("Ingrese la primera posición (fila,columna): ")
    pos2 = input("Ingrese la segunda posición (fila,columna): ")
    fila1, col1 = map(int, pos1.split(','))
    fila2, col2 = map(int, pos2.split(','))
    
    valor1 = tabla[fila1][col1]
    valor2 = tabla[fila2][col2]
    
    operacion = input("¿Desea sumar (+) o restar (-)?: ")
    
    if operacion == '+':
        es_num1 = isinstance(valor1, (int, float)) or (isinstance(valor1, str) and valor1.replace('.', '').replace('-', '').isdigit())
        es_num2 = isinstance(valor2, (int, float)) or (isinstance(valor2, str) and valor2.replace('.', '').replace('-', '').isdigit())
        
        if es_num1 and es_num2:
            resultado = float(valor1) + float(valor2)
        else:
            resultado = str(valor1) + str(valor2)       
    elif operacion == '-':
        resultado = float(valor1) - float(valor2)
    else:
        print("Operación no válida")
    tabla[fila][columna] = resultado    