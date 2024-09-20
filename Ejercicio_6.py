"""crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)"""
palabra_usuario = input("introduce una palabra: ")
def es_palidromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]
print(es_palidromo(palabra_usuario))


