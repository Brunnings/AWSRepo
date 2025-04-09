#introduzir 3 numeros
num1 = int(input("Qual o número?"))
num2 = int(input("Qual o número?"))
num3 = int(input("Qual o número?"))
#ordem crescente ou decrescente
ordem = str(input("Escolha uma opção: Crescente ou Decrescente (c / d) :"))

if ordem == "d":
    if num1 > num2 > num3:
        print(num1, " ", num2, " ", num3)
    elif num2 > num3 > num1:
        print(num2, " ", num3, " ", num1)
    elif num3 > num1 > num2:
        print(num3, " ", num1, " ", num2)
    elif num2 > num1 > num3:
        print(num2, " ", num1, " ", num3)
    elif num1 > num3 > num2:
        print(num1, " ", num3, " ", num2)
    elif num3 > num2 > num1:
        print(num3, " ", num2, " ", num1)
    elif num1 == num2 > num3:
        print(num1, " ", num2, " ", num3)
    elif num2 == num3 > num1:
        print(num2, " ", num3, " ", num1)
    elif num1 == num3 > num2:
        print(num1, " ", num3, " ", num2)
    elif num3 > num1 == num2:
        print(num3, " ", num1, " ", num2)
    elif num1 > num2 == num3:
        print(num1, " ", num2, " ", num3)
    elif num3 > num1 == num3:
        print(num1, " ", num3, " ", num2)
    
elif ordem == "c":
    if num1 < num2 < num3:
        print(num1, "<", num2, "<", num3)
    elif num2 < num3 < num1:
        print(num2, "<", num3, "<", num1)
    elif num3 < num1 < num2:
        print(num3, "<", num1, "<", num2)
    elif num2 < num1 < num3:
        print(num2, "<", num1, "<", num3)
    elif num1 < num3 < num2:
        print(num1, "<", num3, "<", num2)
    else:
        print(num3, "<", num2, "<", num1)
else:
    print("Operação inválida.")
    fuasfsuif
    