import random

class Mutador:
    def __init__(self, base_nitrogenada = None, nivel_mutacion = None, origen = None):
        self.base_nitrogenada = base_nitrogenada or random.choice(["A", "T", "C", "G"])
        self.nivel_mutacion = nivel_mutacion or random.choice(["Bajo", "Moderado", "Alto"])
        self.origen = origen or random.choice(["Ambiental", "Laboratorio", "Natural"]) 
        
    def crear_mutante():
        pass   


    def muestra_datos(self):
        print(f"La base nitrogenada a repetirse será: {self.base_nitrogenada}")
        print(f"El nivel de mutación será: {self.nivel_mutacion}")
        print(f"El origen de la mutación será: {self.origen}")



class Virus(Mutador):
    def __init__(self, base_nitrogenada = None, nivel_mutacion=None, origen=None):
        super().__init__(base_nitrogenada, nivel_mutacion, origen)

    def crear_mutante(self, lista_adn_usuario, base_nitrogenada, posicion_inicial):

        try:
            
            # Convertimos la lista de strings en una lista de listas para modificar la matriz
            matriz_adn = [list(fila) for fila in lista_adn_usuario]

            while True:
                x = int(input("Ingrese la posición de la fila\n ---> "))

                if x >= 0 and x <= 5:
                    break
                else:
                    print("Error: Debes ingresar una posición del 0 al 5")
            while True:
                y = int(input("Ingrese la posición de la columna\n ---> "))
                if y >= 0 and y <= 5:
                    break
                else:
                    print("Error: Debes ingresar una posición del 0 al 5")

            match posicion_inicial:

                case "A":         
                    # Modificamos solo la diagonal superior izquierda
                    for i in range(0,4):
                        matriz_adn[i + x][i + y] = base_nitrogenada  # Cambiamos la base en la diagonal

                case "B":
                    # Modificamos solo la diagonal superior derecha
                    for i in range(0,4):
                        matriz_adn[i + x][y - i] = base_nitrogenada  # Cambiamos la base en la diagonal


            # Imprimimos la matriz resultante
            for fila in matriz_adn:
                print(' '.join(fila))

            return matriz_adn
            

        except Exception as e:
            print(f"Error al crear el mutante: {e}")
            return None

        


        
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada=None, nivel_mutacion=None, origen=None):
        # Llamamos al constructor de la clase base (Mutador) con los parámetros correspondientes
        super().__init__(base_nitrogenada, nivel_mutacion, origen)

    def crear_mutante(self, lista_adn_usuario, posicion_inicial, orientacion_de_la_mutacion, base_nitrogenada):
        """
        Realiza una mutación en el ADN dado, según la posición inicial, la orientación y la base nitrogenada.
        """
        # Convertir las secuencias de ADN en una matriz de listas
        matriz = [list(elemento) for elemento in lista_adn_usuario]
        tamaño_matriz = len(matriz)

        try:
            # Validar la posición inicial
            if not (0 <= posicion_inicial[0] < tamaño_matriz) or not (0 <= posicion_inicial[1] < tamaño_matriz):
                raise IndexError("La posición inicial está fuera de los límites de la matriz.")

            # Validar la orientación de la mutación
            if orientacion_de_la_mutacion not in ['H', 'V']:
                raise ValueError("La orientación debe ser 'H' (horizontal) o 'V' (vertical).")

            # Validar la base nitrogenada
            if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                raise ValueError("La base nitrogenada debe ser A, T, C o G.")

            # Realizar la mutación según la orientación
            if orientacion_de_la_mutacion == 'H':
                # Comprobar límites para la mutación horizontal
                if posicion_inicial[1] + 4 > tamaño_matriz:
                    raise IndexError("No hay suficiente espacio horizontal para la mutación.")
                for i in range(4):
                    matriz[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada

            elif orientacion_de_la_mutacion == 'V':
                # Comprobar límites para la mutación vertical
                if posicion_inicial[0] + 4 > tamaño_matriz:
                    raise IndexError("No hay suficiente espacio vertical para la mutación.")
                for i in range(4):
                    matriz[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada

            # Mostrar la matriz resultante
            print("\nMatriz resultante con la mutación:")
            for fila in matriz:
                print(' '.join(fila))

            return matriz  # Devolver la matriz con las modificaciones

        except Exception as e:
            print(f"Error al crear mutante: {e}")


class  Detector: 
    def __init__(self, lista_adn_usuario, contador_mutaciones=0):
        self.lista_adn_usuario = [list(elemento) for elemento in lista_adn_usuario]
        self.contador_mutaciones = contador_mutaciones

    def detectar_mutantes(self, lista_adn_usuario):
        #comprobar horizontal, vertival, diagonal
        mutaciones_detectadas = {
            "horizontal": self.detectar_horizontal(lista_adn_usuario),
            "vertical": self.detectar_vertical(lista_adn_usuario),
            "diagonal izquierda": self.detectar_diagonal_izquierda(lista_adn_usuario),
            "diagonal derecha": self.detectar_diagonal_derecha(lista_adn_usuario)
        }
        
        print(f"Se encontraron esta cantidad de mutaciones: {self.contador_mutaciones}")
        #paso los resultados de las funciones
        self.tipo_mutacion(mutaciones_detectadas)

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
                self.contador_mutaciones += 1
                return True
            else:
                return False
    
    def detectar_vertical(self, lista_adn_usuario):
        #revisar cada columna de la matriz
        for col in range(6):
            columna = ''.join(fila[col] for fila in self.lista_adn_usuario)
            if self.contar_repeticiones(columna) >= 4:
                self.contador_mutaciones += 1
                return True
        return False
    
    def detectar_diagonal_izquierda(self, lista_adn_usuario):
    
    # Diagonales superiores (comenzando desde la primera columna)
        for i in range(3):  # Recorrer primeras 3 filas
            diagonal = ''.join(lista_adn_usuario[i + j][j] for j in range(6 - i))
            
            if self.contar_repeticiones(diagonal) >= 4:
                self.contador_mutaciones += 1
                return True

    

        return False
    
    def detectar_diagonal_derecha(self, lista_adn_usuario):
    
    # Diagonales superiores (comenzando desde la última columna)
        for i in range(3):  # Recorrer primeras 3 filas
            diagonal = ''.join(lista_adn_usuario[j][5 - (i + j)] for j in range(6 - i))
            
            if self.contar_repeticiones(diagonal) >= 4:
                self.contador_mutaciones += 1
                return True

    

        return False
            
    def tipo_mutacion(self, mutaciones_detectadas):
        #identificar y mostrar los tipos
        tipos_detectados = [tipo for tipo, detectado in mutaciones_detectadas.items() if detectado]
        if not tipos_detectados:
            print ("No se detecto ninguna mutacion.")
        else:
            print (f"Se detectaron las siguientes mutaciones: {', '.join(tipos_detectados)}.")      
            


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

                    
    def sanar_mutantes(self, lista_adn_usuario):  #Analizamos el ADN
        detector = Detector(lista_adn_usuario)
        #metodo detectar
        comprobacion = detector.detectar_mutantes(lista_adn_usuario)
        if (comprobacion == False):
            for fila in lista_adn_usuario:
                print(' '.join(fila))  
                
            print("El ADN administrado no posee mutacion")
            
        else:
            self.cambiar_estado()  # Estado activo del sanador

        while True:
            # Generar un nuevo ADN aleatorio SIN mutaciones
            letras = ["A", "C", "G", "T"]
            nuevo_adn = []
            valido = True  # Bandera para comprobar si el ADN generado es válido

            for i in range(6):
                fila = []
                for j in range(6):
                    letra = random.choice(letras)
                    # Comprobaciones al insertar la letra
                    if (
                        j >= 3 and fila[j-1] == fila[j-2] == fila[j-3] == letra or  # Mutación horizontal
                        i >= 3 and nuevo_adn[i-1][j] == nuevo_adn[i-2][j] == nuevo_adn[i-3][j] == letra or  # Mutación vertical
                        i >= 3 and j >= 3 and nuevo_adn[i-1][j-1] == nuevo_adn[i-2][j-2] == nuevo_adn[i-3][j-3] == letra or  # Diagonal principal
                        i >= 3 and j <= 2 and nuevo_adn[i-1][j+1] == nuevo_adn[i-2][j+2] == nuevo_adn[i-3][j+3] == letra  # Diagonal secundaria
                    ):
                        valido = False  # Marcamos que no es válido y salimos del bucle
                        break
                    fila.append(letra)

                if not valido:
                    break

                nuevo_adn.append(''.join(fila))

            if valido:  # Si el ADN generado no tiene mutaciones, salimos del bucle
                lista_adn_usuario[:] = nuevo_adn
                break

        # Imprimimos el ADN sano y finalizamos la sanación
        print("ADN sano generado:")
        for fila in lista_adn_usuario:
            print(' '.join(fila))
        self.cambio_energia()
        self.sanador_inactivo()
            
        

class Comprobacion:
    def __init__(self):
        pass
    
    def comprobaciones(self):
        pass