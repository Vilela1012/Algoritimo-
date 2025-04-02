opcao = input("Digite a opcao que deseja calcular: \n a-quadrado \n b-retangulo \n c-triangulo opcao:")

match opcao:
    case "a":
        lado = float(input("Digite o lado: "))
        altura = float(input("Digite a altura: "))
        print(f"A área do quadrado é de {lado * altura} metros quadrados.")
    case "b":
        lado = float(input("Digite o lado: "))
        altura = float(input("Digite a altura: "))
        print(f"A area do retangulo é de {lado * altura} metros quadrados.")
    case "c":
        lado = float(input("Digite o lado: "))
        altura = float(input("Digite a altura: "))
        print(f"A area do triangulo é de {lado + altura / 2} metros quadrados.")
