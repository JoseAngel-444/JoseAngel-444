#Definir si un año es biciesto 
Año = int(input("Por favor ingrese el año")) #Año de nacimiento

if Año % 4 == 0 and (Año % 100 !=0 or Año % 400 ==0):
    
    print("Este año es biciesto")
else:
    print("El año no es biciesto")

