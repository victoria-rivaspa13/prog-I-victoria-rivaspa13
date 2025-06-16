# Una función que reciba una tupla y un set, u que devuelva un set con los elementos de la tupla que no estan en el set, y un set con todos los elementos de la tupla que estén repetidos
def ej1(t,s):
    s2 = {}
    for elem in t:
        if elem not in s2:
            s2.add(elem)

# Una función que reciba un string y devuelva una lista con los caracteres del string que no estén repetidos
def ej2(string):
    lista = []
    for elem in string:
        if string.count(elem) == 1:
            lista.append(elem)
    print(lista)

## DICCIONARIOS
# Una función que reciba una lista de nombres y una lista de notas(ambas de igual tamaño). Luego, que devuelva un diccionario donde cada nombre sea una clave y una nota su valor
def ej3(nombres, notas):
    diccionario = dict()
    for i in range (len(nombres)):
        diccionario[nombres[i]] = notas[i]
    print(diccionario)

# Una función que reciba un diccionario con nombres de alumnos, y para cada alumno una lista de 3 notas. Debe calcular el promedio de cada alumno, y debe devolver 1 diccionario con los alumnos aprobados (tienen más de 4 en todas las notas), y su promedio correspondiente, y por otro lado, una lista con los alumnos que deben recuperar algo
def ej4(diccionario):
    aprobados = dict()
    desaprobados = []
    for alumno, nota in diccionario.items():
        promedio = sum (nota) / len(nota)
        if promedio > 4:
            aprobados[alumno] = promedio
        else:
            desaprobados.append(alumno)
    return aprobados, desaprobados

## CLASE JUAN LONGO
# Write a Python program thata takes a dictionary of student names and their
def find_max(diccionario):
    a = ""
    max = 0
    for key, value in diccionario.items():
        if value > max:
            max = value
            a = key
    return a

# Given a dictionary, write a Python program to reverse the dictionary (swap)
def reverse_dict(diccionario):
    a = {}
    for key, value in diccionario.items():
        if value in a:
            a[value]+=k
        else:
            a[value] = key
    return a

# Write a Pythong program that takes a string and counts the frequency of ea
def word_frequency(words):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
print(word_frequency(["apple", "banana", "apple", "cherry", "orange", "banana", "apple"]))



