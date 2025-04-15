#input número para fatorial
numf = int(input("Por qual número deseja realizar o fatorial: "))
#Cálculo do fatorial e imprimir, tanto em caso de número não aplicável, como o resultado
if numf < 0:
    print("Não existem fatoriais para valores não positivos.")
else:
    fatorial = 1
    while numf > 0:
        fatorial *= numf
        numf -= 1
    print(f"Fatorial: {fatorial}")