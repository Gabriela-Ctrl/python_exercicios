def exibir_menu():
    print("Selecione uma das opções:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")
    print()

def obter_opcao():
    while True:
        exibir_menu()
        opcao = input("Digite o número da sua escolha: ") #solicita ao usuário que insira a opção desejada.

        if opcao == "1":
            print("\nEu estou estudando Python!\n")
            break
        elif opcao == "2":
            print("\nEu estou estudando PHP!\n")
            break
        elif opcao == "3":
            print("\nEu estou estudando Java!\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n") #Se o usuário digitar uma opção inválida, o programa exibe uma mensagem de erro e repete o menu.

if __name__ == "__main__":
    obter_opcao()