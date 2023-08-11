print('                       Bem vindo a Sorveteria do KEVELLY CABRAL RIBEIRO')
print('----------------------------------------------------------------------------------------------')
print('------------------------------------------CARDÁPIO--------------------------------------------')
print('|    Nº de Bolas |    Sabor Tradicional (TR) |   Sabor Premium(PR)  |    Sabor Especial(ES)  |')
print('|         1      |            R$6,00           |          R$7,00    |              R$8,00    |')
print('|         2      |            R$10,00          |          R$12,00   |              R$14,00   |')
print('|         3      |            R$12,00          |          R$17,00   |              R$20,00   |')
print('----------------------------------------------------------------------------------------------')
valor_final=0
while True:
    sabor_sorv1=0
    sabor_sorv2=0
    sabor_sorv3=0
    sabor_sorv4=0
    sabor_sorv5=0
    sabor_sorv6=0
    sabor_sorv7=0
    sabor_sorv8=0
    sabor_sorv9=0
    sabor_sorv = input('Entre com o sabor desejado (TR/PR/ES) :')
    if sabor_sorv !="tr" and sabor_sorv!="pr" and sabor_sorv !="es" and sabor_sorv !="TR" and sabor_sorv!="PR" and sabor_sorv !="ES":
     print('sabor invalido.Tente novamenete')
     continue
    bolas_sorv = input('Entre com o número de bolas de sorvete desejado (1/2/3) :')
    if bolas_sorv != '1'  and bolas_sorv !='2' and bolas_sorv !='3':
        print('quantidade inválida.Tente novamente')
        continue
    if sabor_sorv == 'tr' and bolas_sorv == '1' :
        sabor_sorv1 = sabor_sorv1 + 6
        valor_final = valor_final + 6
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv1))
    if sabor_sorv == 'tr' and bolas_sorv == '2':
        valor_final = valor_final + 11
        sabor_sorv2 = sabor_sorv2 + 11
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv2))
    if sabor_sorv == 'tr' and bolas_sorv == '3':
        valor_final = valor_final + 15
        sabor_sorv3 = sabor_sorv3 + 15
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv3))
    if sabor_sorv == 'pr' and bolas_sorv == '1':
        valor_final = valor_final + 7
        sabor_sorv4 = sabor_sorv4 + 7
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv4))
    if sabor_sorv == 'pr' and bolas_sorv == '2':
        valor_final = valor_final + 12
        sabor_sorv5 = sabor_sorv5 + 12
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv5))
    if sabor_sorv == 'pr' and bolas_sorv == '3':
        valor_final = valor_final + 17
        sabor_sorv6 = sabor_sorv6 + 17
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv6))
    if sabor_sorv == 'es' and bolas_sorv == '1':
        valor_final = valor_final + 8
        sabor_sorv7 = sabor_sorv7 + 8
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv7))
    if sabor_sorv == 'es' and bolas_sorv == '2':
        valor_final = valor_final + 14
        sabor_sorv8 = sabor_sorv8 + 14
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv8))
    if sabor_sorv == 'es' and bolas_sorv == '3':
        valor_final = valor_final + 20
        sabor_sorv9 = sabor_sorv9 + 20
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv9))
    if (sabor_sorv == 'TR' and bolas_sorv == '1'):
        sabor_sorv1 = sabor_sorv1 + 6
        valor_final = valor_final + 6
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv1))
    if sabor_sorv == 'TR' and bolas_sorv == '2':
        valor_final = valor_final + 11
        sabor_sorv2 = sabor_sorv2 + 11
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv2))
    if sabor_sorv == 'TR' and bolas_sorv == '3':
        valor_final = valor_final + 15
        sabor_sorv3 = sabor_sorv3 + 15
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv3))
    if sabor_sorv == 'PR' and bolas_sorv == '1':
        valor_final = valor_final + 7
        sabor_sorv4 = sabor_sorv4 + 7
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv4))
    if sabor_sorv == 'PR' and bolas_sorv == '2':
        valor_final = valor_final + 12
        sabor_sorv5 = sabor_sorv5 + 12
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv5))
    if sabor_sorv == 'PR' and bolas_sorv == '3':
        valor_final = valor_final + 17
        sabor_sorv6 = sabor_sorv6 + 17
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv6))
    if sabor_sorv == 'ES' and bolas_sorv == '1':
        valor_final = valor_final + 8
        sabor_sorv7 = sabor_sorv7 + 8
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv7))
    if sabor_sorv == 'ES' and bolas_sorv == '2':
        valor_final = valor_final + 14
        sabor_sorv8 = sabor_sorv8 + 14
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv8))
    if sabor_sorv == 'ES' and bolas_sorv == '3':
        valor_final = valor_final + 20
        sabor_sorv9 = sabor_sorv9 + 20
        print('Você pediu 1 BOLA de sorvete no sabor TRADICIONAL : R${}'.format(sabor_sorv9))
    mais_pedido = input('Deseja pedir mais alguma coisa ?(s/n)')
    if(mais_pedido == 's' or mais_pedido == 'S'):
     continue
    if(mais_pedido == 'n' or mais_pedido == 'N'):
     break
print('O preço final é de : {},00 R$ AGRADECENDO PELA COMPRA  KEVELLY CABRAL RIBEIRO'.format(valor_final))

