for _ in range(1, 99999999):
    menu = int(input("Escolha uma opção:\n1 - Criar \n2 - Atualizar \n3 - Eliminar \n4 - Sair\n"))
    if menu == 1:
        print("A criar ficheiro.")
    elif menu == 2:
        print("A atualizar sistema.")
    elif menu == 3:
        print("A eliminar ficheiro.")
    elif menu == 4:
        print("A desligar o sistema.")
        break
    else:
        print("Opção inválida.")