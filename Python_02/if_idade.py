#Variaveis
nome = input("Informe o seu nome: ")
idade= int(input("Informe a sua idade: "))

#Verifica idade
if idade >=18:
    print("Olá {nome}! Você tem {idade} anos. Então, você é maior de idade")
else: print(f"Olá {nome}! Você tem {idade} anos. Então, você é menor de idade")