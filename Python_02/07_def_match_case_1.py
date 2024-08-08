dia = input("Indique o dia da semana: ")


#função fim de semana
def dia_da_semana(dia):
    match dia:
        case "Domingo" | "Sábado":
            return "Fim de semana"
      
        case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
            return "Dia útil"
      
        case _:
            return "Valor Inválido"

# Exibe o resultado da função
print(dia_da_semana(dia))