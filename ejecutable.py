import clases

print("""¡Bienvenido! Te voy a pedir que ingreses una secuencia de ADN con las iniciales de las 4 bases nitrogenadas, tiene que ser 6 secuencias de 6 iniciales 
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
    print("ADN ingresado correctamente:", lista_adn_usuario)

    # Bucle para seleccionar qué hacer con el ADN
    while True:
        accion_a_realizar = input("""¿Qué deseas hacer con el ADN ingresado?
        -------------------------------------------------
            A - DETECTAR MUTACIONES
            B - MUTARLO
            C - SANARLO
        -------------------------------------------------    
            ---> """).upper()

        # Condición de salida del bucle while
        if accion_a_realizar in ["A", "B", "C"]:
            break
        else:
            print("Error: Debes ingresar A, B o C.")

    print("Acción elegida:", accion_a_realizar)

    match accion_a_realizar:
        case "A":
            # Detectar Mutaciones
            detector = clases.Detector(lista_adn_usuario)
            detector.detectar_mutantes(lista_adn_usuario)
            
        case "B":
            # Preguntar al usuario qué tipo de mutación quiere hacer (radiación o virus)
            mutacion = input("""¿Quieres crear una radiación (A) o un virus (B)?
                            ---> """).upper()

            if mutacion == "A":
                # Solicitar datos para la mutación de radiación
                base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (A, T, C, G): ").upper()
                if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                    print("Base nitrogenada no válida.")
                else:
                    orientacion_de_la_mutacion = input("Ingrese la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
                    if orientacion_de_la_mutacion not in ['H', 'V']:
                        print("Orientación no válida.")
                    else:
                        try:
                            # Solicitar la posición inicial de la mutación
                            posicion_inicial = input("Ingrese la posición inicial (fila, columna): ")
                            posicion_inicial = tuple(map(int, posicion_inicial.split(',')))

                            # Validar la posición antes de llamar al método
                            if not (0 <= posicion_inicial[0] < len(lista_adn_usuario)) or not (0 <= posicion_inicial[1] < len(lista_adn_usuario[0])):
                                print("Posición fuera de los límites de la matriz.")
                            else:
                                # Instanciar la clase Radiacion y pasar los parámetros
                                radiacion = clases.Radiacion()  # Instanciar la clase Radiacion
                                # Llamar al método 'crear_mutante' pasando las variables correctas
                                radiacion.crear_mutante(lista_adn_usuario)
                        except ValueError:
                            print("Entrada de posición inválida.")
                        
            elif mutacion == "B":
                # Instanciar la clase Virus
                virus = clases.Virus()
                virus.crear_virus(lista_adn_usuario)
            else:
                print("Opción incorrecta")

        case "C":
            # Enviar el ADN a la clase Sanador para corregir el ADN
            sanador = clases.Sanador()  # Instanciando la clase
            sanador.sanar_mutantes(lista_adn_usuario)  # Enviando ADN para su análisis  

    # Preguntar si el usuario quiere seguir usando el programa
    salir = input("""¿Quieres seguir usando el programa? S/N
                ---> """).upper()
    if salir == "N":
        print("Saliendo del programa")
        break
    else:
        continue          
