Texto = "Buenos dias definiendo un parametro en una funcion"
#Funcion sin parametros
def Mensaje():
    N1= int(input("Ingresar el primer numero"))
    N2= int(input("Ingresar el segundo numero"))
    Calcularmayor(N1,N2)
    Positivo(N1,N2)

#Funcion con parametros
def Calcularmayor(Num1,Num2):
    if Num1>Num2:
        print("El primer numero es el mayor")
    elif Num1==Num2:
        print("Son numeros iguales")
    else:
        print("El segundo numero es el mayor")

def Positivo(P1,P2):
    if P1>0 and P2>0:
        print("Numeros positivos")

    elif P1<0 and P2<0:
        print("Son negativos")
    else:
        print("Al menos uno de los numeros no es positivo")


Mensaje() 