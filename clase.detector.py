class  Detector: 
    def __init__(self, lista_adn_usuario, longitud_mutacion=4):
        self.lista_adn_usuario = lista_adn_usuario
        self.longitud_mutacion = longitud_mutacion

    
    def detectar_mutantes(self):
        #comprobar horizontal, vertival, diagonal
        return(self.detectar_horizontal()or self.detectar_vertical()or self.detectar_diagonal)
    
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

    def detectar_horizontal(self):
        #revisar cada fila de la matriz
        return any(self.contar_repeticiones(fila) >= self.longitud_mutacion for fila in self.lista_adn_usuario)
    
    def detectar_vertical(self):
        #revisar cada columna de la matriz
        for col in range(len(self.lista_adn_usuario[0])):
            columna = [self.lista_adn_usuario[fila][col]] 
            for fila in range(len(self.lista_adn_usuario)):
                if self.contar_mutaciones(columna) >= self.longitud_mutacion:
                    return True
                else:
                    return False
                
    def detectar_diagonal(self):
        #comrpobar diagonal de izquierda a derecha y derecha a izquierda
        for i in range(len(self.lista_adn_usuario)):
            for j in range(len(self.lista_adn_usuario[0])):
                #de izquierda a derecha
                if i + self.longitud_mutacion <= len(self.lista_adn_usuario) and j + self.longitud_mutacion <= len(self.lista_adn_usuario[0]):
                    diagonal_id = [self.lista_adn_usuario[i+j][j+k] for k in range(self.longitud_mutacion)]
                    if self.contar_mutaciones(diagonal_id) >= self.longitud_mutacion:
                        return True
                    #de derecha a izquierda
                    if i + self.longitud_mutacion <= len(self.lista_adn_usuario) and j - self.longitud_mutacion >= -1:
                        diagonal_di = [self.lista_adn_usuario[i+k][j-k] for k in range(self.longitud_mutacion)]
                        if self.contar_mutaciones(diagonal_di) >= self.longitud_mutacion:
                            return True
                        else: 
                            return False
                        

