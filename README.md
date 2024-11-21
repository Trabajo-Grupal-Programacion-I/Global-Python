# Global-Python
Trabajo global Python ADN

Este programa analiza, detecta, y manipula secuencias de ADN representadas en una matriz de 6x6. Cada base nitrogenada del ADN está representada por las letras A, T, C, y G. El programa permite realizar las siguientes acciones:

La secuencia de ADN ingresada debe ser de la siguiente forma(no necesariamente en mayusculas): AAAAAA,AAAAAA,AAAAAA,AAAAAA,AAAAAA,AAAAAA.

Detección de Mutaciones: Identifica si existen mutaciones en el ADN ingresado. Una mutación ocurre cuando una base nitrogenada se repite al menos 4 veces consecutivas en una misma fila, columna o diagonal (horizontal, vertical o diagonal).
El programa te indicara con un mensaje cuantas y cuales mutaciones contiene tu secuencia de ADN.

Mutación de ADN: Modifica la matriz de ADN generando nuevas mutaciones según los parámetros especificados.
Podras generar mutaciones en tu ADN, puede generar un virus (mutaciones diagonales) especificando la base nitrogenada que quieran repetir y desde que posicion generarla teniendo en cuenta que las posiciones para filas y columnas comienzan en 0 y terminan en 5 ejemplo(0,0) representa la primer fila y la primer columna.
En el caso de cirus tambien tendran la opcion de generar una diagonal de izquierda a derecha y de derecha a izquierda.
Tmabien podran generar una radiacion (mutaciones diagonales y verticales) eligiendo en que direccion desean y desde que posicion.

Sanación de ADN: En caso de que el ADN contenga mutaciones, se genera un nuevo ADN aleatorio que cumple con las restricciones, asegurándose de que no existan mutaciones.

Integrantes: 
Lucas Norton
German Marino
Julian Santos
Manuel Crespo
Ignacio Navarria
