ope_num=input('qual tipo de operacao deseja usar multiplicaçao(*)divisao(/)adiçao(+)ou subtração(-)')
if(ope_num == '*' or '+' or '/' or '-'):
    number_1 = float(input('Digite um numero:'))
    number_2 = float(input('Digite outro numero'))
while (ope_num != 's'):
    if(ope_num=='*'):
        result=number_1 * number_2
        print(result)
    elif(ope_num=='+'):
        result=number_1 + number_2
        print(result)
    elif(ope_num=='/'):
        result=number_1 / number_2
        print(result)
    elif(ope_num=='-'):
        result=number_1 - number_2
    else:
        print('nao foi possivel identificar')
    ope_num = input('qual tipo de operacao deseja usar multiplicaçao(*)divisao(/)adiçao(+)ou subtração(-)')
    if (ope_num == '*' or '+' or '/' or '-'):
        number_1 = float(input('Digite um numero:'))
        number_2 = float(input('Digite outro numero'))

