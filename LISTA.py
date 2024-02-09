Tupla = (2,4,6)
Fecha = ( 9,"Febrero",2024)

print(Tupla)
print(Fecha)

Palabras = int(input("Cuantas palabras desea agregar"))

if Palabras < 1:
    print("No es valido")
else:
    Lista = []
    for i in range(Palabras):
        Palabras = input(f"Escriba la palabra {i+1}")
        Lista += [Palabras]
        print(f"La lista creada es: {Lista}")