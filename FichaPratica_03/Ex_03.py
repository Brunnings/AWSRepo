Jog1 = int(input("Jogador 1, escolha um número entre 1 e 100: "))
tentativa = 0
for _ in range(99999999):
    if Jog1 < 1 or Jog1 > 100:
        print("Número inválido. Tente novamente.")
        break
    tentativa += 1
    print(f"Tentativa nº {tentativa}")
    Jog2 = int(input("Jogador 2, qual o número, entre 0 e 100, que o jogador 1 digitou: "))
    if Jog2 < Jog1:
        print("Seu número é menor que o número que o jogador 1 digitou. Tente novamente.")
    elif Jog2 > Jog1:
        print("Seu número é maior que o número que o jogador 1 digitou. Tente novamente.")
    else:
        print("Parabéns, acertou!")
        break