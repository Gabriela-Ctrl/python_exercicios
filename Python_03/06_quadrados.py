numero = 0

# Cabeçalho das colunas
print("Nro\tQuad\tCubo")

# Loop para calcular os quadrados e cubos de 0 a 50
while numero <= 50:
    quadrado = numero ** 2
    cubo = numero ** 3
    # Imprimindo os resultados com tabulação
    print(f"{numero}\t{quadrado}\t{cubo}")
    # Incrementando o contador
    numero += 1