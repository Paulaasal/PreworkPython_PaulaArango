# Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
lista_numeros =[]
entrada_usuario = input("introduce una lista de números enteros, separados por espacios: ")
lista_numeros = entrada_usuario.split(" ")

  
def contar_pares_impares(numeros):
  pares= 0
  impares = 0
  for numero in numeros:
    numero_int = int(numero)
    if numero_int % 2 == 0:
      pares += 1
    else:
      impares += 1
  return pares, impares

pares, impares = contar_pares_impares(lista_numeros)
print (f"En la lista ingresada hay {pares} numeros pares y {impares} números impares.")
