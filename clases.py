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

    def crear_mutante(self, lista_adn_usuario:list, base_nitrogenada:str, posicion_inicial:tuple, direccion:str):
        
        while True:
                    
                if not base_nitrogenada in ["A", "C", "T", "G"]:
                    print("Error: Debes ingresar A, C, T, G.")
                    base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                elif not direccion in ["A", "B"]:
                    print("Error: Debes ingresar A o B") 
                    direccion = input("""¿Que deseas hacer con el ADN ingresado?
                    -------------------------------------------------
                        A-MODIFICAR DE IZQUIERDA A DERECHA
                        B-MODIFICAR DE DERECHA A IZQUIERDA
                    -------------------------------------------------    
                            ---> """).upper()   
                else:
                    break
        
        x = posicion_inicial[0]
        y = posicion_inicial[1]
                        
        try:
            
            # Convertimos la lista de strings en una lista de listas para modificar la matriz
            matriz_adn = [list(fila) for fila in lista_adn_usuario]

            while True:
                
                if x >= 0 and x <= 5:
                    break
                else:
                    print("Error: La posicion de la fila tiene que tener valores entre 0 y 5")
                    x = int(input("Ingrese la posición de la fila\n ---> "))
            while True:
                
                if y >= 0 and y <= 5:
                    break
                else:
                    print("Error: La posicion de la columna tiene que tener valores entre 0 y 5")
                    y = int(input("Ingrese la posición de la columna\n ---> "))

            imprimir = True
            match direccion:

                case "A":     #comprobacion diagonal izquierda-derecha  
                    
                    for i in range(0,4):
                        matriz_adn[i + x][i + y] = base_nitrogenada  

                case "B":     #comprobacion diagonal derecha-izquierda
                    
                        for i in range(0,4):
                            matriz_adn[i + x][y - i] = base_nitrogenada  
                            check = y-i

                        if (check < 0):
                            imprimir = False
                        
            if imprimir:
                for fila in matriz_adn:
                    print(' '.join(fila))
            else:
                print("Error al crear el mutante: Alguno de los valores ingresados esta fuera de rango")
                
            return matriz_adn
            
        except Exception:
            print("Error al crear el mutante: Alguno de los valores ingresados esta fuera de rango")
            return None

                
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada=None, nivel_mutacion=None, origen=None):
        super().__init__(base_nitrogenada, nivel_mutacion, origen)

    def crear_mutante(self, lista_adn_usuario:list, posicion_inicial:tuple, orientacion_de_la_mutacion:str, base_nitrogenada:str):
        # Convertir las secuencias de ADN en una matriz de lista
        matriz = [list(elemento) for elemento in lista_adn_usuario]
        tamaño_matriz = len(matriz)
        
        while True:
                    
                if not base_nitrogenada in ["A", "C", "T", "G"] :
                    print("Valor de base nitrogenada incorrecto")
                    base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                elif not orientacion_de_la_mutacion in ["H", "V"]:
                    print("Valor de orientacion incorrecto")
                    orientacion_de_la_mutacion = input("Ingrese la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
                elif not (0 <= posicion_inicial[0] < len(lista_adn_usuario)) or not (0 <= posicion_inicial[1] < len(lista_adn_usuario[0])):
                    print("Posición fuera de los límites de la matriz.")
                    posicion_inicial = input("Ingrese la posición inicial (fila, columna): ")
                    posicion_inicial = tuple(map(int, posicion_inicial.split(',')))    
                else:
                    break
                            
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

            for fila in matriz:
                print(' '.join(fila))

            return matriz  

        except Exception as e:
            print(f"Error al crear mutante: {e}")


class  Detector: 
    def __init__(self, lista_adn_usuario:list, contador_mutaciones=0):
        self.lista_adn_usuario = [list(elemento) for elemento in lista_adn_usuario]
        self.contador_mutaciones = contador_mutaciones

    def detectar_mutantes(self, lista_adn_usuario):
        #comprobar horizontal, vertical, diagonal
        mutaciones_detectadas = {
            "horizontal": self.detectar_horizontal(lista_adn_usuario),
            "vertical": self.detectar_vertical(lista_adn_usuario),
            "diagonal izquierda": self.detectar_diagonal_izquierda(lista_adn_usuario),
            "diagonal derecha": self.detectar_diagonal_derecha(lista_adn_usuario)
        }
        
        print(f"Los distintos tipos de mutaciones encontradas son {self.contador_mutaciones}")
        #paso los resultados de las funciones
        self.tipo_mutacion(mutaciones_detectadas)
        
        if True in [self.detectar_horizontal(lista_adn_usuario),self.detectar_vertical(lista_adn_usuario),
                    self.detectar_diagonal_izquierda(lista_adn_usuario),self.detectar_diagonal_derecha(lista_adn_usuario)]:
            return True
        else:
            return False
        
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
        for i in range(3):  
            diagonal = ''.join(lista_adn_usuario[i + j][j] for j in range(6 - i))
            
            if self.contar_repeticiones(diagonal) >= 4:
                self.contador_mutaciones += 1
                return True

        return False
    
    def detectar_diagonal_derecha(self, lista_adn_usuario):
    # Diagonales superiores (comenzando desde la última columna)
        for i in range(3):  
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
                    
    def sanar_mutantes(self, lista_adn_usuario:list):  #Analizamos el ADN
        detector = Detector(lista_adn_usuario)
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
                valido = True 

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
                            valido = False  
                            break
                        fila.append(letra)

                    if not valido:
                        break

                    nuevo_adn.append(''.join(fila))

                if valido:  # Si el ADN generado no tiene mutaciones, salimos del bucle
                    lista_adn_usuario[:] = nuevo_adn
                    break

            print("ADN sano generado:")
            for fila in lista_adn_usuario:
                print(' '.join(fila))
            self.cambio_energia()
            self.sanador_inactivo()
