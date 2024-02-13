Persona = {
    "Nombre":"Jose Angel",
    "Apellido":"Arrieta",
    "Estatura":1.64,
    "Edad":18,
    "Email":"arrietajoseangel50@gmail.com",
    "CiudadNac":"Monteria",
    "Genero":["Masculino","Femenino","Otro"]
}
print(Persona)
#Mostrar un elemento del diccionario
print(f"El nombre de la persona es:", {Persona["Nombre"]})
#Agregar elemento al diccionario
Persona["Telefono"]=3006819670
print(Persona)
#Modificar valor del elemento del diccionario
Persona["Telefono"]=246985
print(Persona)
#Modificar la clave del elemento
Persona["Celular"]=Persona.pop("Telefono")
print(Persona)
#Eliminar un elemento del diccionario
del Persona["Celular"]
print(Persona)

#Integrar los items de las calves y valores 
for Clave,Valor in Persona.items():
    print(Clave, ":", Valor)