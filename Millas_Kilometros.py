# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
def valor():
  millas = float(input("introduce el número de millas que deseas convertir a Kilómetros "))
  return millas

def millas_kilomentros(millas):
  kilometros = millas * 1.60934
  return kilometros

millas = valor ()
kilometros = millas_kilomentros(millas)

print(f"{millas} millas son {kilometros} kilometros")