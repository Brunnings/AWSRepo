#digitar valor do salário
sal = float(input("Qual o seu salário? "))
#cálculo do imposto a pagar
if sal <= 15000:
    imposto = 0.20 * sal
elif sal > 15000:
    imposto = 0.30 * sal
#imprimir o valor do salário e do imposto
print("O seu salário é ", sal, "euros.")
print("O valor do imposto a pagar é ", imposto, "euros.")