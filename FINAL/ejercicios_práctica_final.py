def last_name_first_letter(apellido, letra):
    if apellido[0].lower() < letra.lower():
        print(f"El apellido {apellido} comienza con una letra que está antes de la {letra}")
    elif apellido[0].lower() > letra.lower():
        print(f"El apellido {apellido} comienza con una letra que está después de la {letra}")
    else:
        print(f"El apellido {apellido} comienza con la letra {letra}")

def name_key(nombre, apellido):
    apellido = apellido[:3]
    nombre = nombre[:-1]
    resultado = apellido + nombre
    return resultado

def agregar_fruta(lista, nueva_fruta):
    lista.append(nueva_fruta)
    return lista

def agregar_color(lista, color, posicion):
    posicion = int(posicion)
    lista.insert(posicion, color)
    return lista

def agregar_lista(lista_de_listas, lista):
    lista_de_listas.append(lista)
    return lista_de_listas

def eliminar_elementos(lista):
    del lista[2:5]
    return lista

def eliminar_elementos_por_valor(lista):
    for elemento in lista:
        if lista.count(elemento) > 1:
            lista.remove(elemento)
    return lista

def find_min(lista):
    min = lista[0]
    for num in lista:
        if num < min:
            min = num
        else:
            num += 1
    return min

def find_key_min_map(diccionario):
    min_value = 9999
    min_key = None
    for k, v in diccionario.items():
        if v < min_value:
                min_value = v
                min_key = k
    return min_key

