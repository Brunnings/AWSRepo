#input grades
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
#notas têm que ser entre 0 e 20
if nota1 < 0 or nota2 < 0 or nota3 < 0 or nota1 > 20 or nota2 > 20 or nota3 > 20:
    print("Nota inexistente")
    exit()
#calculo de média ponderada
media = (nota1 * 0.25 + nota2 * 0.35 + nota3 * 0.40)
#imprimir aprovado ou chumbado
if media >= 9.5:
    print("Aprovado")
else:
    print("Chumbado")