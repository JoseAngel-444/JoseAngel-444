def Rango():

    Año1 = int(input("Ingrese el primer año"))
    Año2 = int(input("Ingrese el segundo año"))
    Contador(Año1,Año2)

def Contador(Año1,Año2):

        Bic = 0
        Bic1 = 0
        for i in range (Año1,Año2+1):
              
         if i % 4 == 0 and i % 100 != 0:
             Bic += 1
             print(f"{i} es bisiesto")

        else:
            Bic1 += 1
            print(f"{i} no es bisiesto")

            print(f"Hay {Bic} bisiestos")
            print(f"Hay {Bic1} que no son bisiestos")
Rango()