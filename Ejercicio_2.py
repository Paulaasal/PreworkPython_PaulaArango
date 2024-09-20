#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
plato_1= 32
plato_2= 12
plato_3= 6
mi_lista = [plato_1,plato_2,plato_3]


def suma_platos(precios_propina):
  total = 0
  for precio in precios_propina:
    total += precio
    monto_total_propina = total * 1.15
  return monto_total_propina

print(suma_platos(mi_lista))





















