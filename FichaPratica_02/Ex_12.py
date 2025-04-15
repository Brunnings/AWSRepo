#input dos limites máximo e minimo
max = int(input("Qual o limite máximo? "))
min = int(input("Qual o limite mínimo? "))
#identificar e imprimir todos os multiplos de 5
while min <= max:
    if min % 5 == 0:
        print(min)
    min += 1