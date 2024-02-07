Frase = input("Por favor ingrese una frase")
Letra = input("Por favor ingresar la letra a buscar")
ContLetra = 0

for i in Frase:
    if i == Letra:
        ContLetra += 1
print("La letra '%s' aparece %2i veces en la frase '%s'."%(Letra,ContLetra,Frase))