def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 3:
                return 40
            elif 3 <= peso < 10:
                return 50
            elif 10 <= peso < 30:
                return 60
            elif 30 <= peso < 50:
                return 70
            else:
                print("Cão acima ou com peso igual 50kg não é permitido.")
        except ValueError:
            print("Valor inválido. Digite um número válido para o peso.")


def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro curto,médio,longo(c/m/l): ").lower()
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:

            print("Opção inválida.")



def cachorro_extra():
    extra = 0
    while True:
        try:
            print('------------------------SERVIÇOS EXTRAS------------------------')
            print('1 - cortar unhas')
            print('2 - escovar os dentes')
            print('3 - limpar as orelhas')
            print('0 - não adicionar mais nenhum serviço adicional ou finalizar ')
            adicional = int(input("Digite o código do serviço adicional : "))

            if adicional == 0:
                return extra
            elif adicional == 1:
                extra += 10
            elif adicional == 2:
                extra += 12
            elif adicional == 3:
                extra += 15
            else:
                print("Opção inválida. Digite um código válido para o serviço adicional.")
        except ValueError:
            print("Valor inválido. Digite um código válido para o serviço adicional.")

print("Bem-vindo ao sistema de cobrança do Petshop KEVELLY CABRAL RIBEIRO!")
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()
total = base * multiplicador + extra
print("\n--- Resumo da cobrança ---")
print("preço base por peso do cachorro:", base)
print("Multiplicador:", multiplicador)
print("Valor dos extras:", extra)
print("Total a pagar:", total)
