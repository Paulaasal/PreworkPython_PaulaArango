# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
def valor():
  celsius = float(input("Indica los grados Celsius que deseas convertir a Fahrenheit "))
  return celsius

def celsius_to_fahrenheit(celsius):
  fahrenheit= (celsius * 9/5 +32)
  return fahrenheit

celsius = valor()
fahrenheit= celsius_to_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")














