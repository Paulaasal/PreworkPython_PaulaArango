
# Definir funciones para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
  return a / b

def operaciones():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

while True:
    operaciones()
    opcion = input("Introduce el número de la operación que deseas realizar (o '5' para salir): ")
    if opcion == '5':  
        break

    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    if opcion == '1':
        print(f"El resultado de la suma es: {sumar(a, b)}")
    elif opcion == '2':
        print(f"El resultado de la resta es: {restar(a, b)}")
    elif opcion == '3':
        print(f"El resultado de la multiplicación es: {multiplicar(a, b)}")
    elif opcion == '4':
        print(f"El resultado de la división es: {dividir(a, b)}")
    else:
        print("Opción no válida")
    
    print()  