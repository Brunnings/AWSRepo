#input operações bancarias
operacao = str(input("Operação bancária: \n1. Crédito\n2.Debito\n3.Sair\n"))
salIni = abs(float(input("Saldo inicial: ")))
valMov = abs(float(input("Valor a movimentar: ")))
salFin = 0
#operações bancárias
if operacao == "1":
    salFin = salIni + valMov
elif operacao == "2" and salIni > valMov:
    salFin = salIni - valMov
elif operacao == "2" and salIni < valMov:
    salFin = salIni
else:
    exit()
#imprimir operações
if salFin != salIni:
    print("Saldo inicial: ", salIni, "\nValor movimentado: ", valMov, "\nSaldo atual: ", salFin)
else:
    print("Saldo inicial: ", salIni, "\nValor movimentado: ", valMov, "\nOperação inválida. Saldo insuficiente: ", salFin, "\nSaldo atual: ", salFin)


