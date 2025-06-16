#Ejercicio 3.1 - Dias a horas
def dias_a_horas(dias):
    if dias >= 0:
        horas = dias * 24
        print(horas)
    else:
        print("Número erróneo de días ingresados")

#Ejercicio 3.2 - Dias a horas con fracciones
def dias_a_horas_fracciones(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"
    else:
        horas = dias * 24
        f"{dias * 24} horas"

#Ejercicio 3.3 - Dias a horas con reutilización

#Ejercicio 3.4 - Concatenar strings
def concatenar(string1, string2):
    resultado = string1 + " " + string2
    print(resultado)

#Ejercicio 3.5- Área rectángulo
def calcular_area(x, y):
    area = x * y
    if area >= 0:
        return area
    else:
        return "El área del rectángulo no puede ser negativa"

#Ejercicio 3.6 - Perímetro rectángulo
def calcular_perimetro(x, y):
    perimetro = 2*(x+y)
    if perimetro >= 0:
        return perimetro
    else:
        return "El perimetro del rectángulo no puede ser negativo"

#Ejercicio 3.7 - Información del rectángulo
def informacion_del_rectangulo(x, y):
    area = calcular_area(x, y)
    perimetro = calcular_perimetro(x, y)

    print(f"Rectángulo con base {x} y altura {y}:")
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

#Ejercicio 3.8 - Invertir la oración
def invertir_string(string):
    resultado = string[::-1]
    print(resultado)

#Ejercicio 3.9 - Es par
def es_par(num):
    if num %2 == 0:
        print("True")
    else:
        print ("False")

#Ejercicio 3.10 - Es palindromo
def es_palindromo(string):
    if string[0] == string[-1]:
        print("True")
    else:
        print("False")

#Ejercicio 3.11 - Calificar estudiante
def calificar_estudiante(puntuacion):
    if puntuacion >= 90:
        print("A")
    elif puntuacion >= 80 and puntuacion <= 89:
        print("B")
    elif puntuacion >= 70 and puntuacion <= 79 :
        print("C")
    elif puntuacion >= 60 and puntuacion <= 69:
        print("D")
    else: print("F")

#Ejercicio 3.12 - Verificar positividad
def verificar_positividad(numero):
    if numero == 0:
        print(f"El número {numero} es cero")
    elif numero > 0:
        print(f"El número {numero} es positivo")
    else:
        print(f"El número {numero} es negativo")
