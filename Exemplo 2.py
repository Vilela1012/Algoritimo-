idade = int(input("Digite a idade: "))

if idade <= 17:
    print("MENOR")
else:
    if idade <= 64:
        print("MAIOR")
    else:
        if idade >= 65:
            print("IDOSO")