  # Inicializa o ID global

# Função que fiz para cadastrar um colaborador
def cadastrar_colaborador(id_global):
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o salário do colaborador: "))
    id_global =  id_global +1
    colaborador = {
        'id': id_global,
        'nome': nome,
        'setor': setor,
        'salario': salario,
    }
    lista_colaboradores.append(colaborador)
    id_global += 1  # Incrementa o ID global
    print("Colaborador cadastrado com sucesso!")
    return id_global # Retorna o novo valor de id_global

# Função que fiz para consultar colaboradores
def consultar_colaborador():
    opcao = int(input(
        "Escolha a opção de consulta:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\nOpção: "))

    if opcao == 1:
        print("Consulta de Todos os Colaboradores:")
        for colaborador in lista_colaboradores:
            print(colaborador)
    elif opcao == 2:
        id_consulta = int(input("Digite o id do colaborador a ser consultado: "))
        encontrados = []
        for colaborador in lista_colaboradores:
            if colaborador['id'] == id_consulta:
                encontrados.append(colaborador)
        if encontrados:
            print("Colaboradores encontrados:")
            for colaborador in encontrados:
                print(colaborador)
        else:
            print("Colaborador não encontrado.")
    elif opcao == 3:
        setor_consulta = input("Digite o setor a ser consultado: ")
        print(f"Colaboradores do setor {setor_consulta}:")
        for colaborador in lista_colaboradores:
            if colaborador['setor'] == setor_consulta:
                print(colaborador)
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
    id_remover = int(input("Digite o id do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
            break
    else:
        print("Colaborador não encontrado.")


# Programa principal
print("Bem-vindo ao Controle de Colaboradores do KEVELLY CABRAL RIBEIRO !")

id_global = 0
lista_colaboradores = []
while True:
    print('-'*30,'Menu:', '-'*30)
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    escolha = int(input("Escolha a opção: "))
    if escolha == 1:
        cadastrar_colaborador(id_global)
        id_global = id_global +1
    elif escolha == 2:
        consultar_colaborador()
    elif escolha == 3:
        remover_colaborador()
    elif escolha == 4:
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida.")
