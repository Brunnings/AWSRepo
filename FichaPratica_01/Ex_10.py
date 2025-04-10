#input data
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
#qual a operacao aritmética desejada
operacao = str(input("Digite a operação desejada (+, -, x, /): "))
#calculo da operação aritmética
if operacao == "+":
    res = num1 + num2
elif operacao == "-":
    res = num1 - num2
elif operacao == "x":
    res = num1 * num2
elif operacao == "/":
    res = num1 / num2
else:
    res = "Operação inválida!"
#imprimir resultado
print("O resultado da operação é:", res)