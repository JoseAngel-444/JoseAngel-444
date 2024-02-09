Ancho = int(input("Ingrese el ancho del rectangulo"))
Altura = int(input("Ingrese la altura del rectangulo"))
Caracter = input("Ingrese el caracter a utilizar")

def Dibujar(An,Al,Letra):
    for i in range(An):
        for j in range(Al):
         print(Letra,end="")
        print()

Dibujar(Ancho,Altura,Caracter)