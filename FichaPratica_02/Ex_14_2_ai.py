numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("Fatorial não é definido para números negativos.")
else:
    fatorial = 1
    i = 1
    while i <= numero:
        # Simula a multiplicação usando somas repetidas
        acumulador = 0
        contador = 0
        while contador < fatorial:
            acumulador += i
            contador += 1
        fatorial = acumulador
        i += 1

    print(f"O fatorial de {numero} é {fatorial}")