#escrever 2 numeros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
#maior números dos dois e mostrar na tela
if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os números são iguais.")
