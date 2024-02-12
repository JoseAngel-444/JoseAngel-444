#Definir las listas
Nombres = []
Notas = []
MB = 0
B = 0
INS = 0
Amejor = []
#Llenar la lista
for x in range (1,5):
    Nom = input(f"Por favor ingrese el nombre del alumno: {x}")
    Nombres.append(Nom)
    Not = int(input(f"Por favor ingresar las notas de los alumnos :{x}"))
    Notas.append(Not)
#Recorrer la lista
for y in range (len(Nombres)):
    print(f"El alumno(A){Nombres[y]}",f"Tiene la nota {Notas[y]}")

    if Notas[y]>=8:
     print("Alumno muy bueno")
     MB+=1
     Amejor.append(Nombres[y])

    else:
        if Notas[y]>=4:
           print("Alumno bueno")
           B+=1

        else:
            print("Alumno no aprueba la materia")
            INS+=1
            print("Listado inicial de los alumnos son: ",Nombres)
#Mostrar solo los alumnos que son alumnos buenos
Eliminar = []
for z in range(len(Notas)):
   if 4 <= Notas[z] <= 7:
      Notas.pop(z)
      Nombres.pop(z)
      Eliminar.append(z)
for d in sorted(Eliminar,reverse=True):
    Notas.pop[d]
    Nombres.pop[d]      


print("Cantidad de alumnos muy buenos son: ",MB)
print("Nombre de los mejores alumnos x nota: ",Amejor)
print("Listado de alumnos",Nombres[z])
