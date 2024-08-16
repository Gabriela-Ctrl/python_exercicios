def main():
    try:
        num1 = float(input("Digite o primeiro número "))
        num2 = float(input("Digite o segundo número "))
    except ValueError:
        print("Insira números válidos")
        return
    
    soma1 = num1 +num2

    print(" ")

    print("Primeira soma efetuada!")

    print(" ")

    try:
        num1 = float(input("Digite o primeiro número "))
        num2 = float(input("Digite o segundo número "))
    except ValueError:
        print("Insira números válidos")
        return

    soma2 = num1 +num2

    print(" ")

    print("Segunda soma efetuada!")

    print(" ")

    try:
        num1 = float(input("Digite o primeiro número "))
        num2 = float(input("Digite o segundo número "))
    except ValueError:
        print("Insira números válidos")
        return
    
    soma3 = num1 +num2

    print(" ")

    print("Terceira soma efetuada!")

    print(" ")

    print(f"O resultado da primeira soma é {soma1}")
    print(f"O resultado da segunda soma é {soma2}")
    print(f"O resultado da terceira soma é {soma3}")

    total = soma1 + soma2 + soma3

    print(" ")

    print(f"O total da soma entre os três valores finais é de {total}!")

if __name__ == "__main__":
    main()