#digitar valor do salário
sal = abs(float(input("Qual o seu salário? ")))
#cálculo do imposto a pagar
if sal <= 15000:
    imposto = 0.20 * sal
elif sal > 15000 and sal <= 20000:
    imposto = 0.30 * sal
elif sal > 20000 and sal <= 25000:
    # 20000 < sal <= 25000
    imposto = 0.35 * sal
else:
    imposto = 0.40 * sal
#imprimir o valor do salário e do imposto
print("O seu salário é ", sal, "euros.")
print("O valor do imposto a pagar é ", imposto, "euros.")