#Código que pida al usuario que ingrese un ADN y pregunte si desea detectar mutaciones, mutarlo o sanarlo. Dependiendo de la respuesta, se deben instanciar 
#las clases necesarias y devolver el ADN final junto con algún mensaje informando al respecto del computo realizado.
import clases

print("""¡Bienvenido! Te voy a pedir que ingreses una secuencia de ADN con las inciales de las 4 bases nitrogrenadas, tiene que ser 6 secuecias de 6 iniciales 
separando cada secuencia con una coma(,).""")

while True:
    # Bucle para solicitar el ADN hasta que se ingrese correctamente
    while True:
        adn_usuario = input("Introduzca una secuencia de ADN: ").upper()
        
        # Removemos los espacios y luego dividimos la entrada por comas
        lista_adn_usuario = adn_usuario.replace(" ", "").split(",")
        
        # Validamos longitud de cada secuencia y que haya exactamente 6 secuencias
        if len(lista_adn_usuario) == 6 and all(len(secuencia) == 6 for secuencia in lista_adn_usuario):
            # Verificamos que cada secuencia solo contenga A, T, C o G
            if all(all(base in "ATCG" for base in secuencia) for secuencia in lista_adn_usuario):
                break  # Salimos del bucle si la entrada es válida
            else:
                print("Error: El ADN debe contener solo las letras A, T, C o G.")
        else:
            print("Error: La secuencia de ADN debe tener exactamente 6 secuencias de 6 letras cada una, separadas por comas.")

    # Confirmamos que el ADN ingresado es correcto
    print("ADN ingresado correctamente")
    for fila in lista_adn_usuario:
            print(' '.join(fila))

    #Bucle para seleccionar que hacer con el ADN
    while True: 
        accion_a_realizar = input("""¿Que deseas hacer con el ADN ingresado?
        -------------------------------------------------
            A-DETECTAR MUTACIONES
            B-MUTARLO
            C-SANARLO
        -------------------------------------------------    
            ---> """).upper()

        #Condicion de salida del bucle while
        if accion_a_realizar in ["A", "B", "C"]:
            break
        else:
            print("Error: Debes ingresar A, B o C.")
            
    print("Acción elegida:", accion_a_realizar)


    match accion_a_realizar:
        case "A":
            #Detectar Mutaciones
            detector = clases.Detector(lista_adn_usuario)
            detector.detectar_mutantes(lista_adn_usuario)
        case "B":
            mutacion = input("""¿Quieres crear una radiacion(A) o un virus(B)?
                            ---> """).upper()
            if mutacion == "A":
                radiacion = clases.Radiacion()
                radiacion.crear_mutante(lista_adn_usuario)
            elif mutacion == "B":
                virus = clases.Virus()
                virus.crear_mutante(lista_adn_usuario)
            else:
                print("Opción incorrecta")
            
        case "C":
            #Envia el ADN a la clase Sanador para corregir el ADN
            sanador = clases.Sanador() #Instanciando la clase
            sanador.sanar_mutantes(lista_adn_usuario) #Enviando ADN para su analisis  

    salir = input("""Quiere seguir usando el programa? S/N
                ---> """).upper()
    if salir == "N":
        print("Saliendo del programa")
        break
    else:
        continue            
