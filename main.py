class persona:
    nombre = str
    edad   = int
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad
        
    def saluda (self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.' 
    
if __name__ == "__main__":
    Persona1 = persona("Diego", 33)
    Persona2 = persona("Carla", 35)
    
    print (Persona1.saluda(Persona2))