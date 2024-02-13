def Registrar():
    #Definimos el diccionario
    Agenda={}
    Respuesta = "S"

    while Respuesta =="S":
        Fecha = input("Ingrese la fecha con formato dd/mm/aa :")
        Lista=[]
        while Respuesta =="S":
            Hora = input("Ingrese la hora de la actividad  : h/m")
            Actividad = input("Ingresar el nombre de la actividad")
            Lista.append((Hora,Actividad))
            Respuesta = input("Desea ingreasar una actividad para la misma fecha? s/n :")
        Agenda[Fecha]=Lista
        Respuesta = input("Desea ingresar otra fecha? s/n :")
    return Agenda
def Mostrar(Agenda):
    print("listado de la agenda")
    for Fecha in Agenda:
        print("Para la fecha :",Fecha)
        for Hora,Actividad in Agenda[Fecha]:
            print(Hora,Actividad)
def Consultarxfecha(Fecha):
    Fecha = input("Ingresar la fecha que quiere consultar sus actividades")
    if Fecha in Agenda:
        for Hora,Actividad in Agenda[Fecha]:
            print(Hora,Actividad)
    else:
        print("No existen actividades para la fecha ingresada")
Agenda=Registrar()
Mostrar(Agenda)
Consultarxfecha(Agenda)
