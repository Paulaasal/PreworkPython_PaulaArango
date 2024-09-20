# Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
dia_semana = {
  "1":"lunes",
  "2":"martes",
  "3":"miercoles",
  "4": "jueves",
  "5":"viernes",
  "6":"sabado",
  "7":"domingo"
  }
numero_dia=(input("Introduce el número del día de la semana "))

if numero_dia in dia_semana:
  print (f"El numero introducido equivale al día {dia_semana[numero_dia]}")
else: 
  print ("Número no valido")
