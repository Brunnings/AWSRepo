#input saldo médio
salMed = float(input("Indique o saldo médio: "))
#cálculo do crédito
if salMed <= 2000:
    credito = salMed * 0
elif 2000 < salMed <= 4000:
    credito = salMed * 0.20
elif 4000 < salMed <= 6000:
