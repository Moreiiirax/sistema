import menus
import bancodedados
import uteis

id_proprietario = 1

def cadastrar():
    global id_proprietario

    novo_proprietario = {

    "id" : None,
    "nome" : None,
    "cpf" : None,
    "imovel" : []
    
    }

    menus.menu_cabecalho()
    novo_proprietario['id'] = id_proprietario

    while True:
        novo_proprietario['nome'] = input('Digite o nome do proprietário: ').strip().capitalize()

        if novo_proprietario['nome'].isdigit():
            print('Digite um nome válido!')
            continue
        break

    while True:
        novo_proprietario['cpf']  = input('Digite o CPF do proprietário: ').strip()

        if not novo_proprietario['cpf'].isdigit():
            print('O CPF deve conter apenas números!')
            continue
        if len(novo_proprietario['cpf']) != 11:
            print('O CPF deve conter 11 dígitos!')
            continue
        break
        
    bancodedados.proprietario.append(novo_proprietario)
    id_proprietario += 1
    uteis.limpar()
    print('Proprietário cadastrado com sucesso!')
    

def listar():
    if bancodedados.proprietario == []:
        print('Ainda não há cadastros nesse banco de dados!')
    else:
        print('|    ID    |                          NOME                          |     CPF     |   IMÓVEIS  |')
        print('------------------------------------------------------------------------------------------------')
        for cadastro in bancodedados.proprietario:
            print(f"""|
            {cadastro['id']:^10}|
            {cadastro['nome']:^56}|
            {cadastro['cpf']:^13}|
            {cadastro['imovel']}|
            """)
            print('------------------------------------------------------------------------------------------------')


def excluir():
    
    if bancodedados.proprietario == []:
        print('Ainda não há Proprietários cadastrados!')
        print('Não será possível fazer a operação!')
    else:
        listar() 

        while True:

            cadastro = int(input('Digite o ID do cadastro que deseja excluir: '))

            for proprietario in bancodedados.proprietario:
                if proprietario['id'] == cadastro:
                    bancodedados.proprietario.remove(proprietario)
                    uteis.limpar()
                    print('Cadastro excluído com sucesso!')
                    return

            print('O ID não foi encontrado na lista!')
 

def editar():
    
    if bancodedados.proprietario == []:
        print('Ainda não há Proprietários cadastrados!')
        print('Não será possível fazer a operação!')
    else:
        
        listar() 
        
        menus.secundario()
        parametro = int(input('Digite o parametro pelo qual deseja editar o cadastro: '))

        match parametro:
            case 1: 
            case 2:
            case 3:
            case 4:
            case 0: #Voltar
                print('......Voltando......')
        while True:

            cadastro = int(input('Digite o ID do cadastro que deseja excluir: '))

            for proprietario in bancodedados.proprietario:
                if proprietario['id'] == cadastro:
                    bancodedados.proprietario.remove(proprietario)
                    uteis.limpar()
                    print('Cadastro excluído com sucesso!')
                    return

            print('O ID não foi encontrado na lista!')


def execute(funcao):

    match funcao:
        case 'cadastrar':
            cadastrar()
        case 'listar':
            listar()
        case 'excluir':
            excluir()
        case 'editar':
            editar()
        
