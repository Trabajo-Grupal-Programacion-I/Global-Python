import clases

print("""¡Bienvenido! Te voy a pedir que ingreses una secuencia de ADN con las inciales de las 4 bases nitrogrenadas, 
    tiene que ser 6 secuecias de 6 iniciales separando cada secuencia con una coma(,).""")

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
            mutacion = input("""¿Quieres crear una radiación (A) o un virus (B)?
                            ---> """).upper()
            
            # Solicitar datos para la mutación
            base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
            posicion_inicial = input("Ingrese la posición inicial (fila, columna): ")
            posicion_inicial = tuple(map(int, posicion_inicial.split(',')))
            if mutacion == "A":
                orientacion_de_la_mutacion = input("Ingrese la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
                
                radiacion = clases.Radiacion()  # Instanciar la clase Radiacion
                        # Llamar al método 'crear_mutante' pasando las variables correctas
                radiacion.crear_mutante(lista_adn_usuario, posicion_inicial, orientacion_de_la_mutacion, base_nitrogenada)
                
            elif mutacion == "B":
                virus = clases.Virus()   # Instanciar la clase Virus
                
                direccion = input("""¿Que deseas hacer con el ADN ingresado?
                    -------------------------------------------------
                        A-MODIFICAR DE IZQUIERDA A DERECHA
                        B-MODIFICAR DE DERECHA A IZQUIERDA
                    -------------------------------------------------    
                            ---> """).upper()
                # Llamar metodo para crear Virus
                virus.crear_mutante(lista_adn_usuario, base_nitrogenada, posicion_inicial, direccion)
            else:
                print("Opción incorrecta")
            
        case "C":
            #Envia el ADN a la clase Sanador para corregir el ADN
            sanador = clases.Sanador()  #Instanciando la clase
            sanador.sanar_mutantes(lista_adn_usuario) #Enviando ADN para su analisis  

    salir = input("""Quiere seguir usando el programa? S/N
                ---> """).upper()
    if salir in ["N", "NO"] :
        print("Saliendo del programa")
        break
    else:
        continue            
