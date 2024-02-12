# Lista para guardar los nombres de los conductores
Nombreconductores = ["Jose", "Johan", "Sofia"]

# Lista para guardar los kilómetros que realizan cada día de la semana
kms = [
    [110, 180, 120, 145, 110, 155, 160],  # Lunes
    [189, 186, 254, 163, 152, 112, 150],  # Martes
    [156, 530, 420, 840, 450, 660, 270],  # Miércoles
    [135, 45, 160, 60, 573, 585, 320],  # Jueves
    [142, 360, 560, 70, 30, 95, 210],  # Viernes
    [155, 85, 330, 180, 250, 10, 220],  # Sábado
    [162, 380, 95, 54, 250, 210, 320],   # Domingo
]

#Lista (“Totalkms”) con los kilómetros totales que realiza cada conductor
Totalkms = [sum(Fila) for Fila in kms]

# Mostrar la lista con los nombres de conductores y los kilómetros que han realizado
for i in range(len(Nombreconductores)):
    print(f"{Nombreconductores[i]}: {Totalkms[i]} km")