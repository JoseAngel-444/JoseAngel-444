TurnoMañana = 0
TurnoTarde = 0
TurnoNoche = 0

for i in range (6):
    Edad = int(input("Por favor ingrese la edad del estudiante del turno mañana: "))
    TurnoMañana += Edad

for i in range(7):
    Edad = int(input("Por favor ingrese la edad del estudiante del turno tarde: ")) 
    TurnoTarde += Edad

for i in range(12):
    Edad = int(input("Por favor ingrese la edad del estudiante del turno noche: "))
    TurnoNoche += Edad

    PromedioMañana = TurnoMañana / 6
    PromedioTarde = TurnoTarde / 7
    PromedioNoche = TurnoNoche / 12

print("Promedio de edades del turno mañana: ",PromedioMañana)
print("Promedio de edades del turno tarde: ",PromedioTarde)
print("Promedio de edades del turno noche: ",PromedioNoche)

if PromedioMañana > PromedioTarde and PromedioMañana > PromedioNoche:
    print("El turno mañana tiene un promedio de edades mayor")

elif PromedioTarde > PromedioMañana and PromedioTarde > PromedioNoche:
    print("El turno tarde tiene un promedio de edades mayor")

else:
    print("El turno noche tiene un promedio de edades mayor")