texto = input("Ingrese un texto de más de 5 palabras: ")
t1 = texto.find(" ")
texto = texto[:t1 + 1: ]
t2 = texto.find(" ")
texto = texto[:t2 + 1: ]
t3 = texto.find(" ")
texto = texto[:t3 + 1: ]
t4 = texto.find(" ")
texto = texto[:t4 + 1: ]
t5 = texto.find(" ")
texto = texto[:t5 + 1: ]
promedio = (t1 + t2 + t3 + t4 + t5)/5
print(promedio)

string = input("Ingrese un texto: ")
t1 = string.find(" ")
string = string[:t1 + 1: ]
pal1 = string[:t1]
pal1 = pal1 [::-1]
frase = pal1 + string[t1:]

def ordena(num1, num2):
    if num1 > num2:
        return num2, num1
    else:
        return num1, num2
print(ordena(1,2))

