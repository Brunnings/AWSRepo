#imput constante e fazer 2 constante
num = int(input("Digite um número: "))
min = num - 5
max = num + 5
#loop e print
while min <= max:
    if num != min:
        print(min)
    min += 1