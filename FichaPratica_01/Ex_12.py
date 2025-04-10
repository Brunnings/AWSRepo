#escolha da opção no menu
menu = int(input("Menu: \n1.Criar \n2.Atualizar \n3.Eliminar \n4.Sair \n"))
#operação realizada e impressão
if menu == 1:
    print("A criar novo ficheiro. \nSucesso!")
elif menu == 2:
    print("A atualizar ficheiro. \nSucesso!")
elif menu == 3:
    print("A eliminar ficheiro. \nSucesso!")
elif menu == 4:
    print("Até breve!")
else:
    print("Operação ", menu, "é inválida. Tente novamente.")