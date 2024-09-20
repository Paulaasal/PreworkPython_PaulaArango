#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

from datetime import datetime

año_nacimiento = int(input("introduce el año de tu nacimiento "))
año_actual= datetime.now().year

edad = año_actual - año_nacimiento

print (f"Tu edad es: {edad} años")



  
  



