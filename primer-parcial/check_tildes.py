def check_tilde(oracion):
	tildes = [á, é, í, ó, ú, Á, É, Í, Ó, Ú]
return all(tilde not in tildes for tildes in oracion)

oracion = input("Ingrese una oracion: ")
if check_tilde(oracion):
	return True
else:
	return False