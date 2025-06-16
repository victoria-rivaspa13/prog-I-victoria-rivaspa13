def double_min(set1):
    num1 = 0
    num2 = 0
    for i in set1:
        if (i > num1) and (i > num2):
            num1 = num2
            num2 = i
        elif (i > num1):
            num1 = i
    return num1, num2

def average_min(listas):
    suma = 0
    for lista in listas:
        min_value = lista[0]
        for num in lista:
            if num < min_value:
                min_value = num
        suma += min_value
    promedio = suma/len(listas)
    return promedio
print (average_min([[1, 2, 3], [5, 6, 7], [11, 10, 9]]))

def calculate_grades(mapa):
    my_map = dict()
    for key, value in mapa.items():
        my_sum = 0
        for num in value:
            my_sum += num
        promedio = my_sum/len(value)
        if promedio >= 6:
            my_map[key] = (True, promedio)
        else:
            my_map[key] = (False, promedio)
    return my_map
students = {
        'juan':[6, 2, 4],
        'gaston':[7, 8, 6],
        }
print(calculate_grades(students))

def double_max(set):
    lista = list(set)
    num1 = lista[0]
    num2 = lista[1]
    for i in set:
        if (i > num1) and (i > num2):
            num1 = num2
            num2 = i
        elif (i > num1):
            num1 = i
    return num1, num2
print(double_max({4, 3, 7, 2}))

def double_min(set):
    lista = list(set)
    num1 = lista[0]
    num2 = lista[1]
    for i in set:
        if (i < num1) and (i < num2):
            num1 = num2
            num2 = i
        elif (i < num1):
            num1 = i
    return num1, num2

def ex_sets(set1, set2):
    suma = 0
    for num in set1:
        if num in set2:
            suma += num
        else:
            num + 1
    return suma

set1 = {1, 3, 5, 7, 9}
set2 = {7, 4, 6, 8, 9}
print(ex_sets(set1, set2))

def average_min(listas):
    suma = 0
    for lista in listas:
        min_value = lista[0]
        for num in lista:
            if num < min_value:
                min_value = num
        suma += min_value
    promedio = suma / len(listas)
    return promedio
print(average_min([[1, 2, 3], [5, 6, 7], [11, 10, 9]]))




