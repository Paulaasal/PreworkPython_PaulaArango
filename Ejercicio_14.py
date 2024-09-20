# Calcule el precio final de un artículo después de aplicar un descuento determinado por el usuario.
def precio_articulo():
  precio = float(input("Introduce el precio del artículo "))
  return precio

def precio_descuento(precio,descuento_porcentaje):
  descuento = precio * (descuento_porcentaje/ 100)
  return (precio- descuento)

def precio_final(precio_inicial):
  descuento_porcentaje = float(input("introduce el descuento a aplicar sin el signo de % "))
  return precio_descuento(precio,descuento_porcentaje)

precio = precio_articulo()
precio_final_calculado= precio_final(precio)

print(f"El precio final aplicando el descuento es: €{precio_final_calculado}")


