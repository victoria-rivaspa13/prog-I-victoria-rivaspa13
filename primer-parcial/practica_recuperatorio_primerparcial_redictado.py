def not_in():
    oracion = input("Ingrese una oración: ")
    contiene_a = "á" not in oracion
    contiene_A = "Á" not in oracion
    contiene_e = "é" not in oracion
    contiene_E = "É" not in oracion
    contiene_i = "í" not in oracion
    contiene_I = "Í" not in oracion
    contiene_o = "ó" not in oracion
    contiene_O = "Ó" not in oracion
    contiene_u = "ú" not in oracion
    contiene_U = "Ú" not in oracion
    print(f"No contiene á: {contiene_a}")
    print(f"No contiene é: {contiene_e}")
    print(f"No contiene í: {contiene_i}")
    print(f"No contiene ó: {contiene_o}")
    print(f"No contiene ú: {contiene_u}")
    print(f"No contiene Á: {contiene_A}")
    print(f"No contiene É: {contiene_E}")
    print(f"No contiene Í: {contiene_I}")
    print(f"No contiene Ó: {contiene_O}")
    print(f"No contiene Ú: {contiene_U}")

a = 9
b = False
if a > 1 and a < 9:
    a = 3
    b = True
elif a < 0 or a > 8:
    if a == 9:
        a = 5
        b = True
    else:
        a = 20
    b = False
if b:
    а = 3
else:
    a = 8

def EsMayorDeEdad():
    año = int(input("Ingrese su año de nacimiento: "))
    mes = int(input("Ingrese su mes de nacimiento: "))
    dia = int(input("Ingrese su dia de nacimiento: "))
    dia_actual = 12
    mes_actual = 5
    año_actual = 2023
    edad = año_actual - año
    if mes_actual <= mes and dia_actual <= dia and edad >= 18:
        print("True")
    else:
        print("False")

def elMayorDeTres(num1, num2, num3):
    max = num1
    if num2 > max and num2 > num3:
        max = num2
    elif num3 > max and num3 > num2:
        max = num3
    return max

def compararstrings(s1, s2):
    largo1 = len(s1)
    largo2 = len(s2)
    if largo1 < largo2:
        print(f"El string {s2} es más largo que el string {s1}")
    elif largo1 > largo2:
        print(f"El string {s2} es más corto que el string {s1}")
    else:
        print("Ambos strings tienen la misma longitud")

def slice(texto):
    primera_letra = texto[0].lower()
    ultima_letra = texto[len(texto)-1].lower()
    anteultima_letra = texto[-2].lower()
    primera_letra_negativo = texto[-len(texto)].lower()
    print(primera_letra)
    print(ultima_letra)
    print(anteultima_letra)
    print(primera_letra_negativo)

def n_cara(texto, n):
    cada_n = texto[::n]
    return cada_n

def slice_validate():
    gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
    texto = input("Ingrese un texto: ")
    primeros_dos = texto[:2]
    ultimos_tres = texto[-3:]
    cadena_obtenida = primeros_dos + ultimos_tres
    cadena_obtenida = cadena_obtenida.lower()
    gases_nobles_lower = gases_nobles.lower()
    encontrado = cadena_obtenida in gases_nobles_lower
    print(f"La palabra se encuentra dentro de los gases nobles: {encontrado}")

def sustitucion(texto):
    texto = texto.replace("increíble", "fantástico")
    print(texto)

def imc():
    altura = float(input("Ingrese su altura en m: "))
    peso = float(input("Ingrese su peso en kg: "))
    imc = (peso / altura ** 2)
    if imc < 18.5:
        print(f"Tu IMC es {imc}. Clasificiación: Bajo peso")
    elif imc >= 18.5 and imc < 24.9:
        print(f"Tu IMC es {imc}. Clasificiación: Peso normal")
    elif imc >= 25 and imc < 29.9:
        print(f"Tu IMC es {imc}. Clasificiación: Sobrepeso")
    else:
        print(f"Tu IMC es {imc}. Clasificiación: Obesidad")


def imc():
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    imc = peso / (altura ** 2)

    print(f"Tu IMC es {imc}.")

    if imc < 18.5:
        print("Clasificación: Bajo peso")
        peso_ideal_min = 18.5 * (altura ** 2)
        peso_necesario = round(peso_ideal_min - peso, 2)
        print(f"Necesitas ganar al menos {peso_necesario} kg para alcanzar un IMC normal.")
    elif imc >= 18.5 and imc < 24.9:
        print("Clasificación: Peso normal")
        print("¡Estás en un rango saludable!")
    elif imc >= 25 and imc < 30:
        print("Clasificación: Sobrepeso")
        peso_ideal_max = 24.9 * (altura ** 2)
        peso_necesario = round(peso - peso_ideal_max, 2)
        print(f"Necesitas bajar al menos {peso_necesario} kg para alcanzar un IMC normal.")
    else:
        print("Clasificación: Obesidad")
        peso_ideal_max = 24.9 * (altura ** 2)
        peso_necesario = round(peso - peso_ideal_max, 2)
        print(f"Necesitas bajar al menos {peso_necesario} kg para alcanzar un IMC normal.")

def convertir_temperatura(temperatura, argumento):
    if argumento == "F":
        F = (temperatura * 9/5 + 32)
        print(f"{F} °F")
    elif argumento == "K":
        K = temperatura + 273.15
        print(f"{K} K")

def has_more_as(string):
    cantidad_a = string.count("a")
    no_a = len(string) - cantidad_a
    if cantidad_a > no_a:
        return True
    else:
        return False
print(has_more_as("banana"))

