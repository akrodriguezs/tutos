
class Celda:
    def __init__(self, valor=None, tipo=None, resultado=None):
        self.valor = valor
        self.tipo = tipo
        self.resultado = resultado
        
    def __repr__(self):
        if self.resultado == None:
            return "[   ]"
        return f"[{self.resultado} {self.tipo[:3]}]"