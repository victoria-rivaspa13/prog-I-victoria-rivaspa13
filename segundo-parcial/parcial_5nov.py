def divisors(num):
    resultado = []
    i = 1
    while i<= num:
        if num % i == 0:
            resultado.append(i)
        i += 1
    return resultado
print(divisors(46))


def partidos(lista_de_tuplas):
    diccionario = {}
    for equipo1, goles1, equipo2, goles2 in lista_de_tuplas:
        if equipo1 not in diccionario:
            diccionario[equipo1] = goles1
        else:
            diccionario[equipo1] += goles1

        if equipo2 not in diccionario:
            diccionario[equipo2] = goles2
        else:
            diccionario[equipo2] += goles2

    return diccionario
print(partidos([("River", 3, "Boca", 2), ("Independiente", 1, "Racing", 0), ("River", 1, "Independiente", 2), ("Boca", 3, "Racing", 1)]))

def check_password(password):
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while len(password) >= 6:
        for char in password:
            if " " not in password:
                if "." not in password:
                    if "," not in password:
                        if ";" not in password:
                            if numeros.count(char)>2:
                                if char in letras:
                                    return True
            else:
                return False

def solicitar_password():
    password = input("Ingrese una contraseña: ")
    if check_password(password) == True:
        print("Aceptada")
    else:
        print("Requisitos")

def no_sets(set1, set2):
    suma = 0
    for num in set1:
        if num in set2:
            suma += num
        else:
            suma = suma
    return suma
print(no_sets({3, 5, 2, 7, 6, 4}, {5, 8, 6, 1, -4}))


def no_sets(set1, set2):
    suma = 0
    comun = set1.intersection(set2)
    suma = sum(comun)
    return suma
print(no_sets({3, 5, 2, 7, 6, 4}, {5, 8, 6, 1, -4}))