# Solicitar ao usuário para inserir um número
numero = int(input("Digite um número para verificar se é primo: "))

# Verificar se o número é primo
if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    eh_primo = True
    for i in range(2, numero):  
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")