#Por lo menos 2 atributos que consideren pertinentes.
#Método constructor (init) con sus argumentos para definir los atributos al instanciar un objeto.
#Método sanar_mutantes, encargado de sanar cualquier tipo de mutación. Éste debe tener como argumento la matriz de ADN, revisar si existen mutaciones 
#y, si las hay, generar aleatoriamente un ADN completamente nuevo que no tenga mutaciones y retornarlo. Consejo: esta clase va a necesitar el 
#método detectar_mutante, que ya lo han definido en otra clase!
import random

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