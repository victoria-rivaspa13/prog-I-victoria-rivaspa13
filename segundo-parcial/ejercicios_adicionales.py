#LISTAS
def last_name_first_letter(apellido, letra):
    primera_letra = apellido[0]

    if primera_letra > letra:
        print(f"El apellido {apellido} comienza con una letra posterior a la letra {letra}")
    elif primera_letra < letra:
        print(f"El apellido {apellido} comienz con una letra anterior a la letra {letra}")
    else:
        print(f"El apellido {apellido} comienza con la letra {letra}")

def name_key(nombre, apellido):
    primeras_tres = apellido[:3]
    nombre_sin_ultima = nombre[:-1]
    print(f"{primeras_tres}{nombre_sin_ultima}")

def agregar_fruta(frutas, nueva_fruta):
    frutas.append(nueva_fruta)
    print(f"{frutas}")

def agregar_color(colores, nuevo_color, numero):
    numero = int(numero)
    colores.insert(numero, nuevo_color) #primero la posicion despues el objeto
    print(f"{colores}")

def agregar_lista(listas, nuevo_lista):
    listas.append(nuevo_lista)
    print(f"{listas}")

def eliminar_elementos(lista):
    lista.remove(lista[4])
    lista.remove(lista[3])
    lista.remove(lista[2])
    print(f"{lista}")
#al eliminar elementos de la lista, sus índices cambiarán,
# por lo que hay que eliminar de atrás hacia adelante

def eliminar_elementos_por_valor(lista, string):
    if lista.count(string) > 1:
        lista.remove(string)
    print(f"{lista}")

#LOOPS
def find_min(lista):
    min = 999
    for elemento in lista:
        if elemento < min:
            min = elemento
        else:
            elemento +=1
    print(f"{min}")

def find_key_min_map(diccionario):
    min_value = float(999)
    min_key = 0

    for key, value in diccionario.items():
        if value < min_value:
            min_value = value
            min_key = key
    print(f"{min_key}")

def suma_de_digitos(numero_str):
    suma = 0
    for digito in numero_str:
        suma += int(digito)
    print(f"{suma}")

def categorize_words_by_length(diccionario):
    