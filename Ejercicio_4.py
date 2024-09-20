#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
palabra= (input("escribe tu palabra aqui: "))
vocales = "AEIOUaeiou"
count = 0
for letra in palabra:
  if letra in vocales:
    count += 1
print("el numero de vocales en la palabra es: ", count)




