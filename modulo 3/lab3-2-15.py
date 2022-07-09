#Guadalupe Puente #
#3.2.1.15 LABORATORIO: Hipótesis de Collatz#


C0 = int(input("Enter el numero"))

steps = 0

while C0 !=1:
    if C0 % 2 == 0:
        C0 = int(C0 / 2)
        print(C0)
    else:
        C0 = int(3 * C0 + 1)
        print(C0)

    steps += 1
    
print("steps = ",steps)

