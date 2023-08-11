val1=float(input('Qual o primeiro valor:'))
val2=float(input('Qual o segundo valor:'))
print('digite 1 para somar')
print('digite 2 para multiplicar')
print('digite 3 para dividir')
resp=int(input('Aguardando sua resposta:'))
if(resp==1):
    val1=(val1+val2)
    print('o resultado da soma é : {}'.format(val1))
elif(resp==2):
        val1=(val1*val2)
        print('O resultado da multiplicação é : {}'.format(val1))
if(resp==3):
        val1=(val1/val2)
        print('O resultado da divisao é : {}'.format(val1))
