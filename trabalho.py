print('Bem vindo a loja do KEVELLY CABRAL RIBEIRO')
val_produ=float(input('Digite o valor do produto :'))#local para saber o preço do produto
quanti_produ=int(input('Digite a quantidade desse produto:'))#local para saber a quantidade desse mesmo produto
val_produ = (val_produ*quanti_produ)#A primeira equação para se descobrir o valor sem desconto
print('O valor sem desconto é : R${}.0'.format(val_produ))#coloquei aqui em cima o resultado para deixar de repitir
if(quanti_produ<200):#Aqui é um dos "se" a quantidade estiver dentro dos acordos acontecerá o que estiver abaixo
    print('o valor com desconto será : R${}.0'.format(val_produ))
elif(quanti_produ>200 and quanti_produ<=1000):
    val_produ=(val_produ - val_produ * 5/100)
    print('O valor com desconto será : R${}.0'.format(val_produ))
elif(quanti_produ>1000 and quanti_produ<=2000):
    val_produ=(val_produ - val_produ * 10/100)
    print('O valor com desconto será : R${}.0'.format(val_produ))
else:
    val_produ=(val_produ - val_produ * 15/100)
    print('O valor com desconto será : R${}.0'.format(val_produ))
print('serviço da loja do KEVELLY CABRAL RIBEIRO completo!')
