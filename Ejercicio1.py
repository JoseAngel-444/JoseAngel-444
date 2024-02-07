#alturas de personas y sacar su promedio

Personas = int(input("Ingrese la cantidad de personas: "))
Acumulador = 0


for i in range(Personas):
    Altura = float(input("Ingrese la altura de la persona en metros:"))
    Acumulador += Altura


altura_promedio = Acumulador / Personas


print("La altura promedio de las  personas es: metros")