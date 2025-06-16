texto = "Helio es un gas noble muy utilizado en globos aerostáticos"

parte_a_buscar = texto[:2] + texto[-3:]
print(f"Parte a buscar: {parte_a_buscar}")

gases_nobles = ["helio", "neón", "argón", "criptón", "xenón", "radón"]

if parte_a_buscar.lower() in gases_nobles:
    print(f"{parte_a_buscar} está en la lista de gases nobles.")
else:
    print(f"{parte_a_buscar} no está en la lista de gases nobles.")
