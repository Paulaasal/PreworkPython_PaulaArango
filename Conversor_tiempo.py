# Conversor de Tiempo. Escribe un programa que convierta un número de minutos en horas y minutos.
def valor():
  minutos = float (input("Introduce el número de minutos que deseas convertir a horas"))
  return minutos

def horas_minutos(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes

minutos = valor()
horas, minutos_restantes = horas_minutos(minutos)

print (f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos")




