#input data
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
#maior e menor números dos dois e mostrar na tela o menor e o maior
if num1 > num2:
    print("O maior número é:", num1, "\nO menor número é:", num2)
elif num2 > num1:
    print("O maior número é:", num2, "\nO menor número é:", num1)
else:
    print("Os números são iguais.")
