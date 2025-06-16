productos = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Laptop", "Headphones", "Tablet", "Camera"]

productos_unicos = []
for producto in productos:
    repetido = False
    for unico in productos_unicos:
        if producto == unico:
            repetido = True
            break
    if not repetido:
        productos_unicos.append(producto)

stock = [True, False, True, True, False, True, False, True]

productos_en_stock = []
for i in range(len(productos)):
    if stock[i]:
        productos_en_stock.append(productos[i])

print("Productos únicos:", productos_unicos)
print("Productos en stock:", productos_en_stock)


descripcion_corta = []
for producto in productos:
    descripcion_corta.append("Descripción: " + producto)

precios = [1000, 800, 500, 300, 1000, 150, 500, 600]

precios_descendentes = []
while len(precios) > 0:
    max_precio = precios[0]
    for precio in precios:
        if precio > max_precio:
            max_precio = precio
    precios_descendentes.append(max_precio)
    nuevos_precios = []
    encontrado = False
    for precio in precios:
        if precio == max_precio and not encontrado:
            encontrado = True
        else:
            nuevos_precios.append(precio)
    precios = nuevos_precios

print("Descripción corta:", descripcion_corta)
print("Precios descendentes:", precios_descendentes)


def calcular_promedio(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma / len(lista_numeros)

precio_promedio_resultado = calcular_promedio(precios_descendentes)

print("Precio promedio:", precio_promedio_resultado)
