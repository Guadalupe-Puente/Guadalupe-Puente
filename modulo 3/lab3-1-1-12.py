#Maria Guadalupe Puente Gonzlez#
year = int(input("Introduce un año:"))

if  not (year % 4 == 0):
    print('Año comun')
elif not (year % 100 == 0):
    print('Año Bisiesto')
elif not (year % 400 == 0):
    print('Año comun')

