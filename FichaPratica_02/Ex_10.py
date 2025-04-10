#input limite e salto e variável
max = int(input("Digite o número máximo: "))
salto = int(input("Digite o número do salto: "))
num = 0
#loop e print para salto positivo
if salto > 0:
    while num <= max:
        print(num)
        num += salto
else:
    #aviso de erro caso salto seja negativo
    print("O salto deve ser maior que 0")