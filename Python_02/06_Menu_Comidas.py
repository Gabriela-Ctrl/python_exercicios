print("=====CARDÁPIO=====")
print(" ")

# Array das lojas 
nomes = ["Pizza", "Hamburguer", "Salada"]

# Exibindo Lojas
for i, nomes in enumerate(nomes,1):
    print(f"{i} = {nomes}")
    print(" ")

comida = int(input("Indique a opção desejada: "))

# Seleção de opções
match comida:
    case 1:
        print("Pizza. ")
    case 2:
        print("Hamburguer. ")
    case 3:
        print("Salada. ")
    case _:
        print("Opção inválida")