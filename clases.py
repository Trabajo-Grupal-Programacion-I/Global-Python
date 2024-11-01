#Importación de libreria 'random'
import random
#Creacion de Superclase 'Mutador'
class Mutador:
    def __init__(self, base_nitrogenada, nivel_mutacion, origen):
        self.base_nitrogenada = base_nitrogenada
        self.nivel_mutacion = nivel_mutacion
        self.origen = origen
    #Método para mostrar los datos del mutante al usuario
    def muestra_datos(self):
        print(f"La base nitrogenada a repetirse será: {self.base_nitrogenada}")
        print(f"El nivel de mutación será: {self.nivel_mutacion}")
        print(f"El origen de la mutación será: {self.origen}")
    #Método vacío
    def crear_mutante(self):
        pass


#Selección aleatoria de bases nitrogenadas
base_nitrogenada = ["A", "T", "C", "G"]
base_nitrogenada = random.choice(base_nitrogenada)
#Selección aleatoria de niveles de mutación
nivel_mutacion = ["Bajo", "Moderado", "Alto"]
nivel_mutacion = random.choice(nivel_mutacion)
#Selección aleatoria de origen de mutación
origen_mutacion = ["Ambiental", "Laboratorio", "Natural"]
origen_mutacion = random.choice(origen_mutacion)
