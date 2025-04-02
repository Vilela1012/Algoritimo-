#6. Simulação de Atendimento Telefônico
#O usuário seleciona uma opção de atendimento telefônico:
#1 - Suporte Técnico
#2 - Financeiro
#3 - Cancelamento
#4 - Falar com um atendente#

print("====FUELTECH====")
opcao = int(input("Digite a opção desejada \n 1-Suporte Técnico \n 2-Financeiro \n 3-Cancelamento "
                  "\n 4- Falar com um atendente opção: "))

match opcao:
    case 1:
        print(f"O que você fez de errado?")
    case 2:
        print(f"CALOTEIRO")
    case 3:
        print(f"Cancela não paee")
    case 4:
        print(f"Espera gay")