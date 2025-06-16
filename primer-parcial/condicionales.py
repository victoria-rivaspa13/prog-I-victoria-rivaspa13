#Ejercicio 2.1 - Comparación de booleans
a = True
b = False
c = False

print(f"El valor de a es {a}")
print(f"El valor de b es {b}")
print(f"El valor de c es {c}")

print(f"\nEl valor de a y el valor de b son iguales: {a==b}")
print(f"El valor de b y el valor de c son iguales: {b==c}")
print(f"El valor de a y el valor de c son iguales: {a==c}")

print(f"\nEl valor de a y el valor de b son distintos: {a!=b}")
print(f"El valor de b y el valor de c son distintos: {b!=c}")

#Ejercicio 2.2 - Comparación de números
def comparacion(a, b, c):
    maximo = ""
    if a > b and a > c:
        print (f"El número mayor es: {a}")
    elif b > a and b > c:
        print (f"El número mayor es: {b}")
    else:
        print(f"El número mayor es: {c}")
    if a < b and a < c:
        print(f"El número menor es: {a}")
    elif b < a and b < c:
        print(f"El número menor es: {b}")
    else:
        print(f"El número menor es: {c}")
comparacion(4,-5,2)

#Ejercicio 2.3 - Costo de entradas del parque
def entradas(x,y):
    costo_x = 0
    costo_y = 0
    if x <= 4:
        costo_x = 0
    elif x >= 5 and x <= 17:
        costo_x = 50
    elif x >= 18 and x <= 50:
        costo_x = 30
    else:
        costo_x = 10
    if y <= 4:
        costo_y = 0
    elif y >= 5 and y <= 17:
        costo_y = 50
    elif y >= 18 and y <= 50:
        costo_y = 30
    else:
        costo_y = 10
    costo_total = costo_x + costo_y
    print(f"El costo de entrada para el grupo familiar es de: ${costo_total}")

#Ejercicio 2.4 - Comparación de strings
def tipo_de_dia(dia):
	if dia == "Sabado" or dia == "Domingo":
		return "fin de semana"
	elif dia == "Lunes" or dia == "Martes" or dia == "Miercoles" or dia == "Jueves" or dia == "Viernes":
		return "laborable"
	else:
		return "no es válido"

dia_1 = "Martes"
dia_2 = "Domingo"
dia_3 = "Octodia"

tipo_dia_1 = tipo_de_dia(dia_1)
tipo_dia_2 = tipo_de_dia(dia_2)
tipo_dia_3 = tipo_de_dia(dia_3)

print(f"El día {dia_1} es un día {tipo_dia_1}")
print(f"El día {dia_2} es un día {tipo_dia_2}")
print(f"El día {dia_3} {tipo_dia_3}")

