entrada_usuario = input("introduce una lista de números enteros, separados por espacios: ")
lista_numeros =[]
lista_numeros = entrada_usuario.split(" ")

  
def suma_numeros(numeros):
  total= 0
  for numero in numeros:
    numero_int = int(numero)
    total += numero_int
  return total

total = suma_numeros(lista_numeros)
print (f"los números dentro de tu lista suman:{total}.")