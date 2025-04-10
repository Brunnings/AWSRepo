#valor em euros multiplo de 5
valor = int(input("Indique o valor das notas: "))
#calculo do numero de notas e print
if valor / 5 == valor // 5:
    duzentos = valor // 200
    cem = (valor % 200) // 100
    cinquenta = ((valor % 200) % 100) // 50
    vinte = (((valor % 200) % 100) % 50) // 20
    dez = ((((valor % 200) % 100) % 50) % 20) // 10
    cinco = (((((valor % 200) % 100) % 50) % 20) % 10) // 5
    print(f"São precisas {duzentos} notas de duzentos, {cem} notas de cem, {cinquenta} notas de cinquenta, {vinte} notas de vinte, {dez} notas de dez e {cinco} notas de cinco.")
else:
    print("Não corresponde a um valor de notas.")
