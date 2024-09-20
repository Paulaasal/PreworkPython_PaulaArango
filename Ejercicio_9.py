# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
def valor():
  dolar= float(input("Qué valor en dolares quieres convertir a euros? "))
  return dolar

def dolar_euro(dolar):
  return dolar * 0.85

dolar = valor()
euro = dolar_euro(dolar)

print(f"Este valor corresponde a: {euro:.2f} euros")

