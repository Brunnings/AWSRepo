#input máximo e minímo
min = int(input("Digite o número inicial: "))
max = int(input("Digite o número máximo: "))
#loop e print/ciclo
#como min já é um número que tem outro significado, por eficiencia, deveramos reatribuir esse valor a outra variável
num = min
while num <= max:
    print(num)
    num += 1