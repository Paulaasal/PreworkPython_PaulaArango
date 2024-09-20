"""Escribe un programa que calcule la suma de todos los números pares del 1 al 100."""
def suma_lista(numeros_pares):
  suma = 0
  for numero in numeros_pares:
    if numero % 2 == 0:
      suma += numero
  return suma
print(suma_lista(range(1, 101)))



  
