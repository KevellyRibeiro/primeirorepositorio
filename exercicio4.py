print('qual seu tipo de instalação?')
print('Digite (1) para residencial ')
print('Digite (2) para comercial')
print('Digite (3) para industrial')
resp=int(input('Estou esperando sua resposta : '))
if(resp>3):
    print('Nao possuimos essas informações')
consum=float(input('Consumiu quantos kw/h?'))
if(resp==1):
 if(consum<=500):
    consum=(consum*0.40)
    print('O valor total a ser pago será de : {}0R$'.format(consum))
elif(consum>500):
    consum=(consum*0.65)
    print('O valor total a ser pago será de : {}0R$'.format(consum))
else:
 if(resp==2):
  if(consum<=100):
    consum=(consum*0.55)
    print('O valor total a ser pago será de : {}0R$'.format(consum))
elif(consum>1000):
    consum=(consum*0.60)
    print('O valor total a ser pago será de : {}0R$'.format(consum))
if(resp==3):
 if(consum<=5000):
    consum=(consum*0.55)
    print('O valor total a ser pago será de : {}0R$'.format(consum))
elif(consum>5000):
    consum=(consum*0.60)
    print('O valor total a ser pago será de : {}0R$'.format(consum))