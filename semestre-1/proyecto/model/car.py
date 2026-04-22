class Car:
   ## crear constructur vacio
    def __init__(self, id=0, color="desconocido", brand="desconocida", no_doors=0):
        self.id = id
        self.color = color
        self.brand = brand
        self.no_doors = no_doors
        
    # representacion del objeto    
    def __repr__(self):
        return f"Car(id={self.id}, color='{self.color}', brand='{self.brand}', no_doors={self.no_doors})"  
    
    def __str__(self):
        return
        
    def arrancar(self):
        return f"El carro {self.brand} ha arrancado."
    
    def detener(self):
        return f"El carro {self.brand} se ha detenido."    