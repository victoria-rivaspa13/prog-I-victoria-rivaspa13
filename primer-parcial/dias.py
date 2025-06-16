dia_1 = "Martes"
dia_2 = "Domingo"
dia_3 = "Octodia"

def tipo_de_dia(dia):
	if dia == "Sabado" or dia == "Domingo":
		return "fin de semana" 
	elif dia == "Lunes" or dia == "Martes" or dia == "Miercoles" or dia == "Jueves" or dia == "Viernes":
		return "laborable"
	else:
		return "no es válido"

tipo_dia_1 = tipo_de_dia(dia_1)
tipo_dia_2 = tipo_de_dia(dia_2)
tipo_dia_3 = tipo_de_dia(dia_3)

print(f"El día {dia_1} es un día {tipo_dia_1}")
print(f"El día {dia_2} es un día {tipo_dia_2}")
print(f"El día {dia_3} {tipo_dia_3}")