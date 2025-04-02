#7. Calculadora Simples
#O usuário escolhe uma operação matemática (+, -, *, /)
#e insere dois números. O programa exibe o resultado.#

opcao = int(input("Digite a opção matemática: \n 1) + \n 2) - \n 3) * \n 4) / "
                  "opcção:"))

match opcao:
    case 1:
       num1 = float(input("Digite o numero 1: "))
       num2 = float(input("Digite o numero 2: "))
       print(f"O valor da soma é de {num1 + num2}.")
    case 2:
        num1 = float(input("Digite o numero 1: "))
        num2 = float(input("Digite o numero 2: "))
        print(f"O valor da subtração é de {num1 - num2}.")
    case 3:
        num1 = float(input("Digite o numero 1: "))
        num2 = float(input("Digite o numero 2: "))
        print(f"O valor da multiplicação é de {num1 * num2}.")
    case 4:
        num1 = float(input("Digite o numero 1: "))
        num2 = float(input("Digite o numero 2: "))
        print(f"O valor da subtração é de {num1 / num2}.")
