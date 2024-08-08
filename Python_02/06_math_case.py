opcao = int(input("Indique a opção desejada: "))

#seleção de opções
match opcao:
    case 1:
        print("Suporte Técnico")
    case 2:
        print("Financeiro")
    case 3:
        print("Nossos Produtos")
    case 4:
        print("Outros assuntos")
    case _:
        print("Opção Inválida")