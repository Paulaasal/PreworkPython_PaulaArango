# Escribe un programa que determina si un año ingresado es bisiesto o no. 
año = int(input("ingresa el año que quieres comprobar si es o no bisiesto: "))
if (año % 4 == 0 and año % 100 !=0)or(año %400 == 0):
  print(f"El año {año} es bisiesto.")
else:
  print (f"El año {año} no es bisiesto")
  
  