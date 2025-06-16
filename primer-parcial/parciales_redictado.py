a = True
b = 9
if not a or b > 4:
    a = False
    b = b-3
    if b > 6:
        a = True
    else:
        b = -b
else:
    b = b * 2
b = b + 1
print(a)
print(b)

def semi_suma(a,b):
    a = a/2
    b = b/2
    print (a+b)

def el_del_medio(num1, num2, num3):
    medio = (num1+num2+num3)/3
    print (medio)

def unir_strings(string1, string2, string3):
    frase = string1 + ", " + string2 + ", " + "y " + string3 + "."
    print(frase)

def has_even_length(some_string):
    lenght = len(some_string)
    if lenght % 2 == 0:
        print ("True")
    else:
        print ("False")

def check_password(password):
    largo = len(password) > 5
    letras = password[0]!=password[-1]
    hashtag = "#" in password
    if largo and letras and hashtag:
        print("True")
    else:
        print("False")

def input_and_print():
    input1 = input("Ingrese un texto: ")
    input2 = input("Ingrese un texto: ")
    input3 = input("Ingrese un texto: ")
    input1 = input1.upper()
    input2 = input2.lower()
    input3 = input3.title()
    resultado = input1 + " " + input2 + " " + input3
    print(resultado)

def check_input():
    numero = int(input("Ingrese un número: "))
    divisible7 = numero % 7
    multiplo5 = numero % 5
    if divisible7 == 0 and multiplo5 == 0:
        print(f"El número {numero} es divisible por 7 y múltiplo de 5")
    else:
        print(f"El número {numero} no es divisible por 7 ni múltiplo de 5")

def esMayorDeEdad():
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
    mayor = num1
    if num2 > mayor and num2 > num3:
        mayor = num2
    elif num3 > mayor and num3 > num2:
        mayor = num3
    print(mayor)
elMayorDeTres(1,2,3)

def compararStrings(string1, string2):
    largo_1 = len(string1)
    largo_2 = len(string2)
    if largo_1 == largo_2:
        print("Ambos strings tienen la misma longitud")
    elif largo_1 > largo_2:
        print(f"El string {string1.lower()} es mayor que {string2.lower()}")
    else:
        print(f"El string {string2.lower()} es mayor que {string1.lower()}")
compararStrings("gato", "PeRro")

a = 10
b = 10.10093
if (a < 0 or a > 8):
    if (a == int(b)):
        a = 1
        b = 20
    else:
        a = 20
elif (a > 1 and a < 9):
    a = 3
if (b == 10):
    a = 7
print(a)
print(b)

def check_password(password):
    sietecaracteres = len(password) >= 7
    letras = password[0]==password[-1]
    simbolo = "*" in password
    if sietecaracteres and letras and simbolo:
        return True
    else:
        return False
print(check_password("neuqu*en"))

def invertFirst(texto):
    primeros_tres = texto[:3]
    primeros_tres_invertidos = primeros_tres[::-1]
    print (primeros_tres_invertidos)
invertFirst("lapicera")

def mezcla(str1, str2, n):
    num = int(n)
    str1_parte = str1[:num]
    str2_parte = str2[-num:]
    resultado = str1_parte + str2_parte
    print(resultado)
mezcla("cabello", "melena", 3)