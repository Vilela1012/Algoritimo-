#5 . Tradutor de Cores

#O usuário informa uma cor em português (vermelho, azul, verde, amarelo),
#e o programa exibe sua tradução para inglês.#

print(f"====SUVINIL====")
cor = input("Digite a cor desejada: ")

match cor:
    case "azul" | "Azul":
        print(f"BLUE")
    case "amarelo" | "Amarelo":
        print(f"YELLOW")
    case "vermelho" | "Vermelho":
        print(f"RED")
    case "verde" | "Verde":
        print(f"GREEN")