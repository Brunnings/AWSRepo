#inserir horas e minutos no formato 24 hr
hor = int(input("HH: "))
min = int(input("mm: "))
#conversão e impressão da hora em formato 12 horas
if hor >= 12 and hor <= 23 and min >= 0 and min <= 59:
    hor -= 12
    print(hor, ":", min, " PM")
elif hor >= 0 and hor <= 11 and min >= 0 and min <= 59:
    print(hor, ":", min, " AM")
else:
    print("Valor de hora ou minuto inexistente no formato 24 horas.")