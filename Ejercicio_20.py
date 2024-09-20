# Crea un programa que sume todos los números en una lista introducida por el usuario

entrada_usuario = list(map(int, input("introduce una lista de números enteros, separados por espacios: ").split()))


def suma_numeros(numeros):
  total = 0
  for numero in numeros:
    total += numero
  return total

total = suma_numeros(entrada_usuario)
print (f"los números dentro de tu lista suman:{total}.")