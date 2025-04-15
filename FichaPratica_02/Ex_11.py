#inserir 5 variáveis
primQuar = 0
segunQuar = 0
terQuar = 0
quatQuar = 0
num = 101
#loop para input de numeros e contagem de quantos estão intervalo
while num >= 0:
    num = int(input("Digite um número: "))
    if num <= 25:
        primQuar += 1
    elif 25 < num <= 50:
        segunQuar += 1
    elif 50 < num <= 75:
        terQuar += 1
    elif 75 < num <= 100:
        quatQuar += 1
#imprimir os resultados
print("[0, 25]:", primQuar, "\n[26, 50]:", segunQuar, "\n[51, 75]:", terQuar, "\n[76, 100]:", quatQuar)