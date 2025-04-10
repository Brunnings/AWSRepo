#definir constantes
soma = 0
iter = 0
num = 1
#soma dos numeros inseridos até o número final e média
while num != -1:
    num = int(input("Digite um número: "))
    if num != -1:
        soma += num
        iter += 1
media = soma / iter
#print media
print("A média é:", media)