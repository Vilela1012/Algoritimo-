valor = float(input("Digite o valor em reais: "))
opcao = input("Digite a opcao: \n a-Dolar \n b-Euro \n c-Libra \n opcao: ")

match opcao:
    case "a":
        print(f"O valor convertido é de {valor / 5.80:.2f} dolares.")
    case "b":
        print(f"O valor convertido é de {valor / 6.17:.2f} euros.")
    case "c":
        print(f"O valor convertido é de {valor / 6.20:.2f} libras.")

