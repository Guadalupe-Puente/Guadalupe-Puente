#2.6.1.11 LABORATORIO: Operadores y expresiones
#Guadalupe Puente
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
mins = mins + dura
#print(mins % 60)
#print(mins // 60)
hour = hour + mins // 60
#print(hour)

print(hour % 24, ":", mins % 60, sep="")