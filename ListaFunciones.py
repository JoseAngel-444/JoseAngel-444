def Ingresar():
    Enteros = []

    for x in range(5):
        Numero = int(input("Ingresar el numero"))
        Enteros.append(Numero)
    Imprimir(Enteros)
    Sumar(Enteros)

def Imprimir(Enteros):
        print("Los datos de la lista son: ")
        for x in Enteros:
         print(x)

def Sumar(Enteros):
    Acum = 0
    for x in Enteros:
        Acum = Acum+x
    print("La suma de los numeros es: ",Acum)

Ingresar()
