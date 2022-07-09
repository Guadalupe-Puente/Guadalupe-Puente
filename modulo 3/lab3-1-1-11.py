#Maria Guadalupe Puente Gonzalez #

"""income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = income*0.18 - 556.02

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
"""
ingreso=float(input("Ingrese el ingreso anual: "))
if ingreso<85528:
    impuesto=0.18*ingreso - 556.02
else: 
    impuesto=14839.02+0.32*(ingreso-85528)

impuesto=round(impuesto, 0)
if impuesto<0:
    impuesto=0.0

print("El impuesto es: ", impuesto, "pesos")