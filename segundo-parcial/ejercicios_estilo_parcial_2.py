#1: Escribe una función reverse_list que, dada una lista, retorne una nueva lista con los elementos en orden inverso. No usar funciones provistas por Python que puedan simplificar la tarea.
def reverse_list(lista):
    return lista[::-1]

#2: Escribe una función find_max que, dada una lista de números, retorne el valor máximo en la lista. No usar funciones provistas por Python que puedan simplificar la tarea.
def find_max(lista):
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val

#3: Escribe una función count_elements que, dada una lista de elementos, retorne un diccionario donde las claves son los elementos de la lista y los valores son el número de veces que cada elemento aparece en la lista. No usar funciones provistas por Python que puedan simplificar la tarea.
def count_elements(lista):
    nuevo_diccionario = dict()
    for num in lista:
        if num not in nuevo_diccionario:
            nuevo_diccionario[num] = 1
        else:
            nuevo_diccionario[num] += 1
    return nuevo_diccionario

#4: Escribe una función filter_even_numbers que, dada una lista de números, retorne una nueva lista que contenga solo los números pares de la lista original. No usar funciones provistas por Python que puedan simplificar la tarea.
def filter_even_numnbers(lista):
    nuevo_diccionario = dict()
    for num in lista:
        if num % 2 == 0:
            nuevo_diccionario.append(num)
        return nuevo_diccionario

#5: Escribe una función product_of_list que, dada una lista de números, retorne el producto de todos los números en la lista. No usar funciones provistas por Python que puedan simplificar la tarea.
def product_list(lista):
    for num in lista:
        producto *= num
    return producto

#6: Escribe una función find_long_words que, dada una lista de palabras y un número n, retorne una nueva lista que contenga solo las palabras cuya longitud es mayor que n. No usar funciones provistas por Python que puedan simplificar la tarea.
def find_long_words(lista, numero):
    nueva_lista = list()
    for palabra in lista:
        if len(palabra) > numero:
            nueva_lista.append(word)
    return nueva_lista

#7: Escribe una función sum_list que, dada una lista de números, retorne la suma de todos los números en la lista. No usar funciones provistas por Python que puedan simplificar la tarea.
def sum_list(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

#8: Escribe una función intersection que, dadas dos listas, retorne una nueva lista que contenga solo los elementos que están en ambas listas. No usar funciones provistas por Python que puedan simplificar la tarea.
def intersection(lista_1, lista_2):
    nueva_lista = list()
    for num in lista_1:
        if num in lista_2 and num not in nueva_lista:
            nueva_lista.append(num)
    return nueva_lista

#9: Escribe una función concatenate_lists que, dadas dos listas, retorne una nueva lista que contenga todos los elementos de ambas listas. No usar funciones provistas por Python que puedan simplificar la tarea.
def concatenate_lists(lista_1, lista_2):
    nueva_lista = list()
    for num in lista_1:
        nueva_lista.append(num)
    for num in lista_2:
        nueva_lista.append(num)
    return nueva_lista

#10: Escribe una función sort_list que, dada una lista de números, retorne una nueva lista con los elementos en orden ascendente. No usar funciones provistas por Python que puedan simplificar la tarea.
def sort_list(lista):
    nueva_lista = lista[:]
    n = len(nueva_lista)
    for i in range(n):
        min_index = i
        for elemento in range(i + 1, n):
            if nueva_lista[elemento] < nueva_lista[min_index]:
                min_index = elemento
        nueva_lista[i], nueva_lista[min_index] = nueva_lista[min_index], nueva_lista[i]
    return nueva_lista

#11: Escribe una función remove_duplicates que, dada una lista, retorne una nueva lista con los elementos únicos, preservando el orden original. No usar funciones provistas por Python que puedan simplificar la tarea.
def remove_duplicates(lista):
    nueva_lista = list()
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista


def tata(string):
    vocales = "a", "e", "i", "o", "u"
    resultado = ""
    for caracter in string:
        resultado += caracter
        if caracter in vocales:
            resultado += "ta"
    return resultado

def simplista(lista):
    resultado = []
    for i in range (len(matriz)):
        if i < len(matriz[i]):
            resultado.append(lista[i])
        else:
            resultado.append(None)
    return resultado

def acceso(lista):
    adultos = 0
    menores = 0
    for age in lista:
        if age < 18:
            menores +=1
        else:
            adultos += 1
    if menores >= 5 * adultos:
        return True
    else:
        return False
print(acceso("4", "8", "2"))


