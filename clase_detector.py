class  Detector: 
    def __init__(self, lista_adn_usuario):
        self.lista_adn_usuario = [list(elemento) for elemento in lista_adn_usuario]

    def detectar_mutantes(self, lista_adn_usuario):
        #comprobar horizontal, vertival, diagonal
        return(self.detectar_horizontal(lista_adn_usuario)or self.detectar_vertical(lista_adn_usuario)or self.detectar_diagonal(lista_adn_usuario))
    
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
                 print("Se encontro una mutacion en horizantal")
                 return True
            else:
                 return False
    
    def detectar_vertical(self, lista_adn_usuario):
        #revisar cada columna de la matriz
        for col in range(6):
            columna = ''.join(fila[col] for fila in self.lista_adn_usuario)
            if self.contar_repeticiones(columna) >= 4:
                 print("Se encontro una mutacion en vertical")
                 return True
        return False
    
    def detectar_diagonal(self, lista_dn_usuario):
        #comrpobar diagonal de izquierda a derecha y derecha a izquierda
        #comprobar de izquierda a derecha
        for i in range(3):
            diagonal = ''.join(self.lista_adn_usuario[i + j][j] for j in range(6 - i))
            if self.contar_repeticiones(diagonal) >= 4:
                print("Se encontro una mutacion en diagonal")
                return True
            else:
                return False
            
        #comprobar de derecha a izquiersa 
        for i in range (1, 6):
            diagonal = ''.join(self.lista_adn_usuario[j][i + j] for j in range (6 - i))
            if self.contar_repeticiones(diagonal) >= 4:
                print("Se encontro una mutacion en diagonal")
                return True
            else:
                return False


            


                        

