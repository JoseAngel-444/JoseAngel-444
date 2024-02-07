N = int(input("Ingrese # de empleados"))
Cont = 0
Cont1 = 0
Gasto = 0

for ini in range(N):
    Sueldo = float(input("Ingresar el valor sueldo del empleado"))
    Gasto = Gasto+Sueldo
    if Sueldo >= 1300000 and Sueldo <=3000000:
        Cont +=1
    elif Sueldo >3000000:
        Cont1 +=1
print("Los gastos de la empresa total",Gasto)
print("Empleados que ganan entre 1.300.000 3.000.000 son:",Cont)
print("Empleados que ganan mas de 3.000.000",Cont1)