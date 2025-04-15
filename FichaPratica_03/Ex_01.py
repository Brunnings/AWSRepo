for _ in range(1, 99999999):
    #Definir variáveis
    n1 = int(input("Digite o primeiro número da operação que deseja efetuar: "))
    op = input("Digite a operação que deseja efetuar (+, -, x, /): ")
    n2 = int(input("Digite o segundo número da operação que deseja efetuar: "))
    #operações e print
    if op == "+":
        print("O resultado da operação é:", n1 + n2)
    elif op == "-":
        print("O resultado da operação é:", n1 - n2)
    elif op == "x":
        print("O resultado da operação é:", n1 * n2)
    elif op == "/":
        if n2 != 0:
            print("O resultado da operação é:", n1 / n2)
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação inválida.")
    continuar = str(input("Deseja continuar? (s/n): "))
    if continuar != "s":
        print("A desligar o sistema.")
        break

