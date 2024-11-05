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

# Creacion de la Subclase "Radiacion"
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, nivel_mutacion, origen, intensidad, tipo_radiacion):
        super().__init__(base_nitrogenada, nivel_mutacion, origen)  # Llama al constructor de la superclase
        self.tamaño_matriz = 6  # Fijo a 6x6
        self.intensidad = intensidad  # Atributo para la intensidad de la radiación
        self.tipo_radiacion = tipo_radiacion  # Atributo para el tipo de radiación
        self.matriz = self.crear_matriz_vacia()  # Crear la matriz vacía

    def crear_matriz_vacia(self):
        # Crea una matriz vacía de 6x6
        return [['-' for _ in range(self.tamaño_matriz)] for _ in range(self.tamaño_matriz)]

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        try:
            # Comprobaciones previas
            if orientacion_de_la_mutacion not in ['H', 'V']:
                raise ValueError("La orientación debe ser 'H' (horizontal) o 'V' (vertical).")
            if not (0 <= posicion_inicial[0] < self.tamaño_matriz) or not (0 <= posicion_inicial[1] < self.tamaño_matriz):
                raise IndexError("La posición inicial está fuera de los límites de la matriz.")

            # Realiza la mutación en la matriz
            if orientacion_de_la_mutacion == 'H':
                # Comprobar límites para la mutación horizontal
                if posicion_inicial[1] + 4 > self.tamaño_matriz:
                    raise IndexError("No hay suficiente espacio horizontal para la mutación.")
                for i in range(4):
                    self.matriz[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada

            elif orientacion_de_la_mutacion == 'V':
                # Comprobar límites para la mutación vertical
                if posicion_inicial[0] + 4 > self.tamaño_matriz:
                    raise IndexError("No hay suficiente espacio vertical para la mutación.")
                for i in range(4):
                    self.matriz[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada

            return self.matriz  # Devolver la matriz con las modificaciones

        except Exception as e:
            print(f"Error al crear mutante: {e}")

# Ejemplo de uso
# Selección aleatoria de bases nitrogenadas
base_nitrogenada = random.choice(["A", "T", "C", "G"])
# Selección aleatoria de niveles de mutación
nivel_mutacion = random.choice(["Bajo", "Moderado", "Alto"])
# Selección aleatoria de origen de mutación
origen_mutacion = random.choice(["Ambiental", "Laboratorio", "Natural"])
# Selección aleatoria de intensidad y tipo de radiación
intensidad = random.choice(["Baja", "Media", "Alta"])
tipo_radiacion = random.choice(["UV", "Ionizante", "Radón"])

# Creación de una instancia de Radiacion
radiacion = Radiacion(base_nitrogenada, nivel_mutacion, origen_mutacion, intensidad=intensidad, tipo_radiacion=tipo_radiacion)

# Creación de un mutante
posicion_inicial = (2, 2)  # Ejemplo de posición inicial
orientacion_de_la_mutacion = random.choice(['H','V'])  # Puede ser 'H' o 'V'
matriz_modificada = radiacion.crear_mutante(base_nitrogenada='C', posicion_inicial=posicion_inicial, orientacion_de_la_mutacion=orientacion_de_la_mutacion)

# Mostrar la matriz resultante
for fila in matriz_modificada:
    print(' '.join(fila))
