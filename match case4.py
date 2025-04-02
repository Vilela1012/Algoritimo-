#4. Cálculo de Desconto por Categoria
# O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis),
# e o programa exibirá o percentual de desconto correspondente.#

print(f"====MARABRAZ====")
opcao = int(input("Digite o protudo comprado: \n 1-Eletrônico \n 2-Roupas \n 3-Alimentos \n 4-Móveis opção: "))

match opcao:
    case 1:
        valor = float(input("Digite o valor do produto: "))
        print(f"O desconto é de: {valor - valor * 0.5} reais.")
    case 2:
        valor = float(input("Digite o valor do produto: "))
        print(f"O desconto é de: {valor - valor * 0.3} reais.")
    case 3:
        valor = float(input("Digite o valor do produto: "))
        print(f"O desconto é de: {valor - valor * 0.1} reais.")
    case 4:
        valor = float(input("Digite o valor do produto: "))
        print(f"O desconto é de: {valor - valor * 0.4} reais.")







