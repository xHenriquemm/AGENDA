AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>> Agenda vazia')

def buscar_contato(contato):
    if contato in AGENDA:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
        print('--------------------------------------------')
    else:
        print('>>>> Contato inexistente')

def ler_detalhes_contato():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print(f'\n>>>> Contato {contato} adicionado/editado com sucesso\n')

def excluir_contato(contato):
    if contato in AGENDA:
        AGENDA.pop(contato)
        salvar()
        print(f'\n>>>> Contato {contato} excluído com sucesso\n')
    else:
        print('>>>> Contato inexistente')

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato, dados in AGENDA.items():
                arquivo.write(f"{contato},{dados['telefone']},{dados['email']},{dados['endereco']}\n")
        print('>>>> Agenda exportada com sucesso')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, telefone, email, endereco = linha.strip().split(',')
                incluir_editar_contato(nome, telefone, email, endereco)
        print('>>>> Contatos importados com sucesso')
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, telefone, email, endereco = linha.strip().split(',')
                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print(f'>>>> Database carregado com sucesso ({len(AGENDA)} contatos)')
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado, criando um novo database.')
        with open('database.csv', 'w') as arquivo:
            pass  # Cria o arquivo vazio
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)

def imprimir_menu():
    print('------------------------------------------')
    print('1 - Criar contato')
    print('2 - Mostrar todos os contatos da agenda')
    print('3 - Buscar contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print('------------------------------------------')


carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        contato = input('Digite o nome do contato: ')
        if contato in AGENDA:
            print('>>>> Contato já existente')
        else:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '2':
        mostrar_contatos()
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        if contato in AGENDA:
            print(f'>>>> Editando contato: {contato}')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        else:
            print('>>>> Contato inexistente')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('>>>> Fechando programa')
        break
    else:
        print('>>>> Opção inválida')
