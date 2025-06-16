def average_list(lista):
    suma = 0
    for i in lista:
        suma += i
        promedio = suma/len(lista)
    print(promedio)

def count_first_characters(diccionario):
    nuevo_diccionario = {}
    for list in diccionario.values():
        for item in list:
            if item[0] not in nuevo_diccionario:
                nuevo_diccionario[item[0].lower()] = 1
            else:
                nuevo_diccionario[item[0].lower()] += 1
    print (nuevo_diccionario)
count_first_characters({
    'category1': ["apple", "banana", "avocado"],
    'category2':["cherry", "blueberry", "blackberry"],
    'category3':["grape", "kiwi", "orange"]
})

def sum_expenses_by_category(lista_de_tuplas):
    nuevo_diccionario = {}
    for tupla in lista_de_tuplas:
        category, price = tupla
        if category not in nuevo_diccionario.keys():
            nuevo_diccionario[category] = price
        else:
            nuevo_diccionario[category] += price
    print(nuevo_diccionario)

sum_expenses_by_category([("Supermercado", 2000), ("Transporte", 1500), ("Supermercado",
3000), ("Transporte", 1000), ("Ocio", 500)])


def ex_sets(set1, set2):
    suma1 = 0
    suma2 = 0
    for i in set1:
        if i not in set2:
            suma1 += i
        else:
            suma1 = suma1
    for i in set2:
        if i not in set1:
            suma2 += i
    suma3 = suma1 + suma2
    return suma3

print(ex_sets({1, 3, 5, 7, 9}, {2, 4, 6, 8, 9}))

def index_of(lista, palabra):
    if palabra in lista:
        for i, p in enumerate(lista):
            if p == palabra:
                return i
    else:
        return -1
print(index_of(["Hola", "Mundo", "Python"], "Mundo"))

def categorize_words_by_initial(diccionario):
    nuevo_diccionario = {}
    for lista in diccionario.values():
        for item in lista:
            if item[0] not in nuevo_diccionario:
                nuevo_diccionario[item[0].lower()] = [item]
            else:
                nuevo_diccionario[item[0].lower()].append(item)
    return nuevo_diccionario


print(categorize_words_by_initial({
    'category1': ["apple", "banana", "avocado"],
    'category2':["cherry", "blueberry", "blackberry"],
    'category3':["grape", "kiwi", "orange"]
}))


def categorize_words_by_initial(diccionario):
    nuevo_diccionario = {}
    for lista in diccionario.values():
        for item in lista:
            inicial = item[0]
            if inicial not in nuevo_diccionario:
                nuevo_diccionario[inicial.lower()] = [item]
            else:
                nuevo_diccionario[inicial.lower()].append(item)
    return nuevo_diccionario

print(categorize_words_by_initial({
    'category1': ["apple", "banana", "avocado"],
    'category2':["cherry", "blueberry", "blackberry"],
    'category3':["grape", "kiwi", "orange"]
}))

def sum_of_expenses_by_category(lista_de_tuplas):
    nuevo_diccionario = {}
    for tupla in lista_de_tuplas:
        categoria, precio = tupla
        if categoria not in nuevo_diccionario:
            nuevo_diccionario[categoria] = precio
        else:
            nuevo_diccionario[categoria] += precio
    return nuevo_diccionario
print(sum_of_expenses_by_category([("Supermercado", 2000), ("Transporte", 1500), ("Supermercado",
3000), ("Transporte", 1000), ("Ocio", 500)]))

def sum_of_expenses_by_category(lista_de_tuplas):
    nuevo_diccionario = {}
    for tupla in lista_de_tuplas:
        categoria, precio = tupla
        valor = 0
        if categoria not in nuevo_diccionario:
            valor = precio
            nuevo_diccionario[categoria] = valor
        else:
            valor += precio
            nuevo_diccionario[categoria] = valor
    return nuevo_diccionario



def unique_char(string):
    resultado = set()
    for palabra in string:
        for letra in palabra:
            if letra not in resultado:
                resultado.add(letra)
            else:
                letra += palabra
    return resultado
print(unique_char({"hello"}))

def unique_char(string):
    resultado = []
    for palabra in string:
        for letra in palabra:
            if letra not in resultado:
                resultado.append(letra)
        else:
            letra += palabra
    resultado.sort()
    return resultado
print(unique_char({"hello"}))

def find_max(diccionario):
    resultado = ""
    maximo = 0
    for nombre, nota in diccionario.items():
        if nota > maximo:
            maximo = nota
            resultado = nombre
    return resultado
print(find_max({'John': 85, 'Emma': 92, 'Sophia': 78}))

def reverse_dict(diccionario):
    resultado = {}
    for key, value in diccionario.items():
        resultado[value] = key
    return resultado
print(reverse_dict({1: 'a', 2: 'b', 3: 'c'}))

# print(unique_words(["Hola Mundo", "Mundo Maravilloso", "Hola a todos", "Bienvenidos al maravilloso mundo de Python"]))

def word_frequency(string):
    frequency = dict()
    for palabra in string:
        if palabra in frequency:
            frequency[palabra] += 1
        else:
            frequency[palabra] = 1
    return frequency
print(word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"]))

def biggest_expense(diccionario):
    max_avg = 0
    max_expense = ''

    for category, costs in diccionario.items():
        if costs:
            average = sum(costs) / len(costs)
            if average > max_avg:
                max_avg = average
                max_expense = category

    return max_expense
print(biggest_expense({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}))

def sum_of_expenses(diccionario):
    resultado = dict()
    for expenses, costs in diccionario.items():
        total = 0
        for cost in costs:
            total += cost
            resultado[expenses] = total
    return resultado
print(sum_of_expenses({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}))

def sum_of_expenses_by_type(diccionario):
    output = dict()
    for expenses, costs in diccionario.items():
        for tipo, cost in costs:
            if tipo in output:
                output[tipo] += cost
            else:
                output[tipo] = cost
    return output

print(sum_of_expenses_by_type({'Food': [("A", 60), ("B", 100), ("A", 20)], 'Transport': [("A", 10), ("B", 50), ("C", 5)], 'Games': [("A", 6), ("B", 24), ("C", 99)]}))


tupla = (1, 2, 3)
print(tupla.index(1))
