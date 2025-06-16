def last_name_first_letter(apellido, letra):
    letras = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    primera_letra_apellido = apellido[0]

    if primera_letra_apellido < letra:
        return "anterior"
    elif primera_letra_apellido > letra:
        return "posterior"
    else:
        return "igual"

def name_key(first_name, last_name):
    last_name[:3]
    first_name[:-1]
    return first_name + last_name

def agregar_fruta[frutas](nueva_fruta):
    return frutas.append(nueva_fruta)

def agregar_color[colores](nuevo_color, posicion):
    return colores.insert (posicion,nuevo_color)

def agregar_lista(lista, nueva_lista):
    return lista.append(nueva_lista)

def eliminar_elementos(lista):
    del lista[2:5]
    return lista

def eliminar_elementos_por_valor(lista):
    for elemento in lista:
        if lista.count(elemento) > 1:
            lista.remove(elemento)
    return lista

# Ejercicio 1 loops
def find_min(numeros):
    min_valor = numeros[0]
    for number in numeros:
        if number < min_valor:
            min_valor = number
    return min_valor
print (find_min([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Ejercicio 2 loops
def find_key_min_map(diccionario):
    min_value = float("inf")
    min_key = None
    for key, value in diccionario.items():
        if value < min_value:
            min_value = value
            min_key = key
    return min_key
print(find_key_min_map({"ingenieria": 100, "abogacia":50, "medicina": 70,"administracion" :10}))

# Ejercicio 3 loops
def suma_de_digitos(numero):
    suma = 0
    for digito in numero:
        suma += int(digito)
    return suma
print(suma_de_digitos("12345"))

# Ejercicio 4 loops
def categorize_words_by_length(diccionario):
    nuevo_diccionario = {}
    for value in diccionario.values():
        for elemento in value:
            element_length = len(elemento)
            if elemento in nuevo_diccionario:
                nuevo_diccionario[element_length].append(elemento)
            else:
                nuevo_diccionario[element_length] = [elemento]
    return nuevo_diccionario
print(categorize_words_by_length({
    "frutas": ["manzana", "pera", "mango"],
    "animales": ["perro", "gato", "elefante"],
    "colores": ["rojo", "azul", "verde"]
}))

# Ejercicio 5 loops
def find_highest_score(lista):
    highest_score = float("-inf")
    highest_score_student = None

    for student, score in lista:
        if score > highest_score:
            highest_score = score
            highest_score_student = student
    return highest_score_student
print (find_highest_score([("Juan", 85), ("Ana", 92), ("Pedro", 88), ("Claudia", 95)]))


numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)



