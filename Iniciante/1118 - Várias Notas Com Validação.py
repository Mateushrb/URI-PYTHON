novo_calculo = 1
while novo_calculo == 1:
    
    nota_valida_1 = 0
    
    while nota_valida_1 != 1:
        nota_1 = float(input())
        if nota_1 >= 0 and nota_1 <= 10:
            nota_valida_1 = 1
        else:
            print("nota invalida")

    nota_valida_2 = 0
    
    while nota_valida_2 != 1:
        nota_2 = float(input())
        if nota_2 >= 0 and nota_2 <= 10:
            nota_valida_2 = 1
        else:
            print("nota invalida")

    media = (nota_1 + nota_2) / 2
    print("media = %0.2f" %(media))
    
    rep = 0
    while rep == 0:
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = float(input())
        if novo_calculo < 1 or novo_calculo > 2:
            rep = 0
        else:
            rep = 1
