#Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
def valores():
  longitud = float(input("Introduce el valor de longitud en cm "))
  ancho = float(input("Introduce el valor del ancho en cm "))
  return longitud, ancho

  
def area_rectangulo(longitud, ancho): 
  return (longitud*ancho)
  
longitud, ancho = valores()
area = area_rectangulo(longitud,ancho)
  
print(f"El área del rectángulo es de {area:.2f} cm²")
  
  