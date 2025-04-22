# Pedir três números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Perguntar a ordem desejada
ordem = input("Escolha a ordem: Crescente (c) ou Decrescente (d): ")

# Ordenar os números
if ordem == "c":
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    print("Ordem crescente:", num1, num2, num3)
elif ordem == "d":
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2
    print("Ordem decrescente:", num1, num2, num3)
else:
    print("Opção inválida.")