# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero_usuario = int(input("Introduce un número: "))
if es_primo(numero_usuario):
    print(f"El número {numero_usuario} es primo.")
else:
    print(f"El número {numero_usuario} no es primo.")


