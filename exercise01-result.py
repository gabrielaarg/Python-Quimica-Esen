listaclientes = []
clientes = 0

while clientes < 500:
    cliente = input("Nombre:")
    producto = input("Su producto es:")
    costo = float(input("Su costo es:"))

registro = dict(cliente=cliente, producto=producto, costo=costo)
listaclientes.append(registro)


# final = input("¿Se agregara otro cliente a el registro?")

# while final != ("Si") or final != ("No")
#    print(La respuesta debe limitarse a"Si"o"No")
#       final = input ("¿Se agregara otro cliente a el registro?")

# if final == ("Si"):
#       clientes += 1
#  else if final == ("No"):
#     break

# for registro in listaclientes:
#   print (registro)

# costostotales = input(“¿Quiere consultar el costo total de el día?” )
# while costostotales != (“Si”) or costostotales != (“No”):
# print(La respuesta debe limitarse a "Si"  o "No")
# 	costostotales = input(“¿Quiere consultar el costo total de el día?” )

# if consultaCostoTotal == ("si"):
#       costos = float(sum(costo))
#      print(costos)
