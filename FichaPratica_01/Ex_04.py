#input data
pos = int(input("Qual a posição do número que quer saber? "))
#pontuação 
if pos < 1:
    print("Posição inexistente.")
elif pos == 1:
    pont = 10
elif pos == 2:
    pont = 8
elif pos == 3:
    pont = 6
elif pos == 4:
    pont = 5
elif pos == 5:
    pont = 4
elif pos == 6:
    pont = 3
elif pos == 7:
    pont = 2
elif pos == 8:
    pont = 1
else:
    print("Posição atual: ", pos, "\n Pontos: Não ganhou pontos.")
#imprimir resultado
print(f"Posição atual: {pos} \n Pontos:  {pont} pontos.")