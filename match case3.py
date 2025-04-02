print(f"====LOGIN====")
nome = input("Digite o seu nome: ").lower()

match nome:
    case "admin":
        print(f"ACESSO TOTAL.")
    case "professor":
        print(f"ACESSO AO AMBIENTE ACADEMICO.")
    case "aluno":
        print(f"ACESSO AO AMBIENTE DE ESTUDOS.")