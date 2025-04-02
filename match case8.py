#8. Sistema de Reserva de Passagens
#O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador)
#e recebe o valor da passagem.#
print(f"BEM VINDO A AZUL")
destino = int(input("Digite o destino: "
                "\n 1) São Paulo "
                "\n 2) Rio de Janeiro"
                "\n 3) Curitiba"
                "\n 4) Salvador opção:"))

match destino:
    case 1:
        print(f"O valor da passagem é de 1.7 bilhões de reais.")
    case 2:
        print(f"O valor da passagem é de 30 centavos.")
    case 3:
        print(f"O valor da passagem é de 40 wuons.")
    case 4:
        print(f"O valor da passagem é de um pino de coca e uma glockada de 30. ")
