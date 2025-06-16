# Cadena de gases nobles y texto dado
gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
texto = "Hello, Aurelio"

# Convertir la cadena de gases nobles a una lista de palabras en minúsculas
gases_nobles_lista = [gas.strip().lower() for gas in gases_nobles.split(',')]

# Obtener los primeros 2 caracteres y los últimos 3 caracteres del texto
parte_a_buscar = texto[:2] + texto[-3:]

# Verificar si la parte obtenida está en la lista de gases nobles (en minúsculas)
encontrado = parte_a_buscar.lower() in gases_nobles_lista

print(f"La palabra se encuentra dentro de los gases nobles: {encontrado}")
