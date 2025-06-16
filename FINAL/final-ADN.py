
adn_secuencia = "ATCGGACTAATCGTT"

def extract (adn):
    fragmentos = [adn[i:i+3] for i in range (0, len(adn) - len(adn) % 3, 3)]
    return fragmentos

def transform (fragmentos):
    arn_resultado = []
    count_a = 0
    count_c = 0
    count_u = 0
    count_g = 0
    for fragmento in fragmentos:
        arn_fragmento = ""
        for nucleotido in fragmento:
            if nucleotido == "G":
                arn_fragmento += "C"
                count_c += 1
            elif nucleotido == "C":
                arn_fragmento += "G"
                count_g += 1
            elif nucleotido == "T":
                arn_fragmento += "A"
                count_a += 1
            elif nucleotido == "A":
                arn_fragmento += "U"
                count_u += 1
            arn_resultado.append(arn_fragmento)
    return [arn_resultado, count_a, count_c, count_g, count_u]


def load(resultados):
    arn = resultados[0]
    count_a = resultados[1]
    count_c = resultados[2]
    count_g = resultados[3]
    count_u = resultados[4]
    print(f"ARN obtenido: {arn}")
    print(f"Cantidad de adenina: {count_a}")
    print(f"Cantidad de citosina: {count_c}")
    print(f"Cantidad de guanina: {count_g}")
    print(f"Cantidad de uracilo: {count_u}")

fragmentos_extraidos = extract(adn_secuencia)
resultados_transformados = transform(fragmentos_extraidos)
load(resultados_transformados)