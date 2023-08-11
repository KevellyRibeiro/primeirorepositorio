print('maça (1)')
print('laranja (2)')
print('manga (3)')
fruta = int(input('Qual fruta você escolhe ? :'))
quanti = int(input('Quantas unidades ?'))
if fruta == 1:
    pagam = quanti * 2.30
    print('o total a ser pago será {}, reais'.format(pagam))
else:
    if fruta == 2:
        pagam = quanti * 3.60
        print('o valor total a ser pago será {}, reais'.format(pagam))
    else:
     if fruta == 3:
      pagam = quanti * 1.85
      print('O valor total a ser pago será {}, reais'.format(pagam))
     else :
       print('escolheu errado')
