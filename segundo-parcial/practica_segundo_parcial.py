def last_name_first_letter(apellido, letra):
    primera_letra = apellido[0]
    if primera_letra > letra:
        resultado = f"El apellido {apellido} comienza con una letra que está después de la {letra}"
    elif primera_letra < letra:
        resultado = f"El apellido {apellido} comienza con una letra que está antes de la {letra}"
    else:
        resultado = f"El apellido {apellido} comienza con la letra {letra}"

    return resultado

def name_key(nombre, apellido):
    primeras_tres_letras = apellido [:3]
    nombre_sin_última = nombre [:-1]
    resultado = primeras_tres_letras + nombre_sin_última
    return resultado

def agregar_fruta(frutas, nueva_fruta):
    frutas.append(nueva_fruta)
    return frutas

def agregar_color(colores, nuevo_color, posición):
    colores.insert(posición, nuevo_color)
    return colores

def agregar_lista(lista, nueva_lista):
    lista.append(nueva_lista)
    return lista

def eliminar_elementos(lista):
    del lista[2:5]
    return lista

def eliminar_elementos_por_valor(lista):
    for elemento in lista:
        if lista.count(elemento) > 1:
        lista.remove(elemento)
    return lista

def find_min(lista):
    min_value = lista[0]
    for elemento in lista:
        if elemento < min_value:
            min_value == elemento
    return min_value










