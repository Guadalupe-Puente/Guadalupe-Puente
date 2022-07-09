#Guadalupe Puente 
#3.4.1.13 LABORATORIO: Lo básico de las listas - Los Beatles
beatles=[]
# paso 1
print("Paso 1:", beatles)
beatles.append("John Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# paso 2
print(" Paso 2:", beatles)

# paso 3
para i en el rango (0,1):
var1=input("ingrese StuSutcliffe para agregarlo a la lista de bandas")
beatles.append(var1)
var2=input("por favor ingrese a Pete Best para agregarlo en la lista de bandas")
beatles.append(var2)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4: ", beatles)

# paso 5
beatles.insert(0,"Ringo starr")
print("Paso 5:", beatles)


# longitud de la lista de prueba
print("The Fab", len(beatles)