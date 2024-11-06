import random

class Mutador:
    def __init__(self, base_nitrogenada = None, nivel_mutacion = None, origen = None):
        self.base_nitrogenada = base_nitrogenada or random.choice(["A", "T", "C", "G"])
        self.nivel_mutacion = nivel_mutacion or random.choice(["Bajo", "Moderado", "Alto"])
        self.origen = origen or random.choice(["Ambiental", "Laboratorio", "Natural"]) 
        
    #base_nitrogenada = base_nitrogenada or random.choice(["A", "T", "C", "G"])
    #nivel_mutacion = nivel_mutacion or random.choice(["Bajo", "Moderado", "Alto"])
    #origen = origen or random.choice(["Ambiental", "Laboratorio", "Natural"])   


    def muestra_datos(self):
        print(f"La base nitrogenada a repetirse será: {self.base_nitrogenada}")
        print(f"El nivel de mutación será: {self.nivel_mutacion}")
        print(f"El origen de la mutación será: {self.origen}")
    
    
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada = None, nivel_mutacion = None, origen = None, tipo_radiacion = None):
        super().__init__(base_nitrogenada, nivel_mutacion, origen)
        self.tipo_radiacion = tipo_radiacion or random.choice(["UV", "Ionizante", "Radón"]) 
        self.tamaño_matriz = 6
        self.matriz = [['-' for _ in range(self.tamaño_matriz)] for _ in range(self.tamaño_matriz)]  # Crear matriz vacía
        
        
    #tipo_radiacion = tipo_radiacion or random.choice(["UV", "Ionizante", "Radón"]) 
    
    def crear_mutante(self, lista_adn_usuario):
        posicion_inicial = (2, 2)  # Ejemplo de posición inicial
        orientacion_de_la_mutacion = random.choice(['H', 'V'])
        base_nitrogenada = self.base_nitrogenada  # Usamos el atributo de la clase
        self.matriz = [list(elemento) for elemento in lista_adn_usuario]

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

            # Mostrar la matriz resultante
            for fila in self.matriz:
                print(' '.join(fila))

            return self.matriz  # Devolver la matriz con las modificaciones

        except Exception as e:
            print(f"Error al crear mutante: {e}")


class  Detector: 
    def __init__(self, lista_adn_usuario):
        self.lista_adn_usuario = [list(elemento) for elemento in lista_adn_usuario]

    def detectar_mutantes(self, lista_adn_usuario):
        #comprobar horizontal, vertival, diagonal
        horizontal = self.detectar_horizontal(lista_adn_usuario)
        vertical = self.detectar_vertical(lista_adn_usuario)
        diagonal = self.detectar_diagonal(lista_adn_usuario)
        
        #paso los resultados de las funciones
        self.tipo_mutacion(horizontal, vertical, diagonal)

    def contar_repeticiones(self, lista_adn_usuario):
        #cuenta cuantas veces se repite una base nitrogenada
        max_repeticiones = 1
        conteo_actual = 1

        for i in range(1, len(lista_adn_usuario)):
            if lista_adn_usuario[i] == lista_adn_usuario[i-1]:
                conteo_actual += 1
            else:
                max_repeticiones = max(max_repeticiones, conteo_actual)
                conteo_actual = 1
        max_repeticiones = max(max_repeticiones, conteo_actual)
        return max_repeticiones
    
    
    def detectar_horizontal(self, lista_adn_usuario):
        #revisar cada fila de la matriz
        for fila in self.lista_adn_usuario:
            if self.contar_repeticiones(fila) >= 4:
                return True
            else:
                return False
    
    def detectar_vertical(self, lista_adn_usuario):
        #revisar cada columna de la matriz
        for col in range(6):
            columna = ''.join(fila[col] for fila in self.lista_adn_usuario)
            if self.contar_repeticiones(columna) >= 4:
                return True
        return False
    
    def detectar_diagonal(self, lista_adn_usuario):
        #comrpobar diagonal de izquierda a derecha y derecha a izquierda
        #comprobar de izquierda a derecha
        for i in range(3):
            diagonal = ''.join(self.lista_adn_usuario[i + j][j] for j in range(6 - i))
            if self.contar_repeticiones(diagonal) >= 4:
                return True
            else:
                return False
            
        #comprobar de derecha a izquiersa 
        for i in range (1, 6):
            diagonal = ''.join(self.lista_adn_usuario[j][i + j] for j in range (6 - i))
            if self.contar_repeticiones(diagonal) >= 4:
                return True
            else:
                return False
            
    def tipo_mutacion(self, detectar_horizontal, detectar_vertical, detectar_diagonal):
        if detectar_horizontal:
            print("Se detecto una mutacion horizontal.")
        elif detectar_vertical:
            print("Se detecto una mutacion vertical.")
        elif detectar_diagonal:
            print("Se detecto una mutacion diagonal.")
        elif detectar_diagonal and detectar_horizontal and detectar_vertical:
            print("Se detectaron mutaciones horizontales, verticales y diagonales.")
        else:
            print("No se detecto ninguna mutacion.")
            
            
#Por lo menos 2 atributos que consideren pertinentes.
#Método constructor (init) con sus argumentos para definir los atributos al instanciar un objeto.
#Método sanar_mutantes, encargado de sanar cualquier tipo de mutación. Éste debe tener como argumento la matriz de ADN, revisar si existen mutaciones 
#y, si las hay, generar aleatoriamente un ADN completamente nuevo que no tenga mutaciones y retornarlo. Consejo: esta clase va a necesitar el 
#método detectar_mutante, que ya lo han definido en otra clase!


class Sanador:
    
    def __init__(self, energia = 100, estado_del_sanador = "Inactivo"):
        self.energia = energia
        self.estado_del_sanador = estado_del_sanador    
    
    
    def cambio_energia(self):
        self.energia =random.choice([20, 40, 60, 80])
        print("La energia restante del sanador es: " + str(self.energia))


    def cambiar_estado(self):  #Cambio de estado del sanador
        if self.estado_del_sanador == "Inactivo":
            self.estado_del_sanador = "Activo"
            print("El sanador esta activo")
        else:
            print("El sanador ya esta en estado activo")

    
    def sanador_inactivo(self):  #Voliendo a estado inactivo el sanador
        if self.estado_del_sanador == "Activo":
            self.estado_del_sanador = "Inactivo"
            print("El sanador esta inactivo")
        else: 
            print("El sanador ya esta en estado inactivo")

                    
    def sanar_mutantes(self, adn):  #Analizamos el ADN
        #metodo detectar
        if ():  
            print("El ADN administrado no posee mutacion") 
        else:
            self.cambiar_estado()  #Estado activo del sanador  
            self.adn_aleatorio(adn)  #Cambiamos el ADN mutado por uno sano
        return

    
    def adn_aleatorio(self,adn):  #Creacion del ADN nuevo
        adn.clear()
        letras = ["A", "C", "G", "T"]
        
        for i in range(6):  
            secuencia = ''.join(random.choice(letras) for i in range(6))
            adn.append(secuencia)
        print(adn)
        self.cambio_energia()
        self.sanador_inactivo()
        
        
        
        #falta metodo detectar y bucle, luego dejar inactivo el sanador y mostrar la energia restante