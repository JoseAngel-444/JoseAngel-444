#solicitar 10 numeros y solicitar su promedio utilizando while

import random

Suma = 0
Cont_Num = 0
 
while Cont_Num < 10:
    Numero = int(input("Por favor ingresa un numero"))
    Suma = Suma+Numero
    
    Cont_Num += 1

    Promedio = Suma / 10
    
    print("La suma de los numeros es:",Suma)
    print("El promedio de los 10 numeros es: ",Promedio)