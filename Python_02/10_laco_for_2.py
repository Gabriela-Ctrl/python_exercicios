print("=====LOJAS=====")
print(" ")

#Array
lojas = ["Santo André", "São Bernardo", "São Caetano", "Diadema"]

#Exibindo Lojas
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")
    print(" ")

    #Escolhendo loja para exibição
    loja_selecionada = int(input("Selecione a loja desejada: "))

    #   Exibindo loja selecionada (caso nçao exista)
    if 1 <= loja_selecionada <= len(lojas):
        print(lojas[loja_selecionada -1])
    else:
        print("Loja inválida")
