#Ejercicio 1.1 - Uso del “not in”
def not_in():
    oracion = input("Ingrese una oracion: ")
    contiene_a = "á" not in oracion
    contiene_e = "é" not in oracion
    contiene_i = "í" not in oracion
    contiene_o = "ó" not in oracion
    contiene_u = "ú" not in oracion
    print("No contiene á:", contiene_a)
    print("No contiene é:", contiene_e)
    print("No contiene í:", contiene_i)
    print("No contiene ó:", contiene_o)
    print("No contiene ú:", contiene_u)

#Ejercicio 1.2 - Uso del “slice” con un carácter
def slice():
    texto = input("Ingrese un texto: ")
    primera_letra = texto[0].lower()
    ultima_letra = texto[len(texto)-1].lower()
    anteultima_letra = texto[-2].lower()
    primera_letra_neg = texto[-len(texto)].lower()
    print(primera_letra)
    print(ultima_letra)
    print(anteultima_letra)
    print(primera_letra_neg)

#Ejercicio 1.3 - Uso del “slice” con orden inverso
def slice_inverted():
    texto = input("Ingrese un texto: ")
    palabra_invertida = texto[::-1]
    print(palabra_invertida)

#Ejercicio 1.4 - Uso del “slice” cada n caracteres.
def slice_n():
    texto = input("Ingrese un texto: ")
    texto_n = texto[::3]
    print(texto_n)

# versión pro
texto = input("Ingrese un texto: ")
caracteres = int(input("Ingrese un número de caracteres: "))
texto_n1 = texto[::caracteres]
print(texto_n1)

#Ejercicio 1.5 - Uso del “slice” validando que la palabra obtenida está contenida en otro string
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

#Ejercicio 1.7 - Modificaciones de los strings.
def edad():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    incremento = 1
    nueva_edad = str(edad + incremento)

    print(nombre, "tiene", nueva_edad, "años")

