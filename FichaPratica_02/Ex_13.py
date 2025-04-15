#inserir número de números na sequência e selecionar constantes
nrNrs = int(input("Quantos números deseja inserir na sua sequência?"))
iter = 2
ordem = "Crescente"
#certeza que o número de números seja favorável à formação de uma sequencia e determinar se essa sequência é crescente ou não e imprimir
if nrNrs > 1:
    num1 = int(input("Introduza um número: "))
    num = num1
    while iter <= nrNrs:
        num1 = int(input("Introduza um número: "))
        if num1 < num:
            ordem = "Não crescente"
        num = num1
        iter += 1
    print(f"{ordem}")
else:
    print("Não é possível gerar uma sequência com menos de dois números")