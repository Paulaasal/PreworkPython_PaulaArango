# Escribe un programa que calcule el índice de Masa corporal (IMC) de una persona
def valores():
  print("Bienvenido. Para calcular tu IMC necesito que me proporciones unos datos")
  peso = float(input("Introduce tu peso en Kg: "))
  altura = float(input("Introduce tu estatura en m: "))
  return peso, altura
  
def calcular_IMC(peso,altura):
  return peso/ (altura ** 2)

peso, altura = valores()
imc = calcular_IMC(peso, altura)

print (f"Tu indice de masa corporal es: {imc:.2f}")

  