def obter_nota(i):
    while True:
        try:
            nota = float(input(f"Informe a sua {i}ª nota: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

# Função principal
def verificar_notas():
    notas = []

    for i in range(1, 5):
        nota = obter_nota(i)
        notas.append(nota)

    media = sum(notas) / 4
    print(f"Sua média final foi de {media:.2f}")

# Execução do programa
verificar_notas()