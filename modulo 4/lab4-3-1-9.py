#Guadalupe Puente#
#4.3.1.9 LABORATORIO: Números primos: ¿Cómo encontrarlos?#

def isPrinceipal (num):
    for i in range (2, int, (1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
    
    for i in range (1, 20):
        id is Principal (i + 1)
        print (i + 1, end = " ")
    print ()