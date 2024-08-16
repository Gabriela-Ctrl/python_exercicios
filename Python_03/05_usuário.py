def obter_nome():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("Nome inválido! O nome deve ter mais de 3 caracteres.\n")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade (entre 0 e 100): "))
            if 0 <= idade <= 100:
                return idade
            else:
                print("Idade inválida! A idade deve estar entre 0 e 100.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.\n")

def obter_salario():
    while True:
        try:
            salario = float(input("Digite seu salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido! O salário deve ser maior que zero.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.\n")

def obter_sexo():
    while True:
        sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Sexo inválido! Digite 'f' para feminino ou 'm' para masculino.\n")

def obter_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido! Digite 's' para solteiro, 'c' para casado, 'v' para viúvo, ou 'd' para divorciado.\n")

def main():
    nome = obter_nome()
    idade = obter_idade()
    salario = obter_salario()
    sexo = obter_sexo()
    estado_civil = obter_estado_civil()

    print("\nInformações válidas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {estado_civil.upper()}")

if __name__ == "__main__":
    main()
