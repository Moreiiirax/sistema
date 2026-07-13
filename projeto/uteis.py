import menus
import os

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def escolhe_instituto():

    menus.menu_instituto()
    opcao = int(input('Digite o valor correspondente: '))

    match opcao:
        case 1: #PROPRIETARIO
            limpar()
            return 'proprietario'
        case 2: #IMOVEL
            limpar()
            return 'imovel'
        case 3: #INQUILINO
            limpar()
            return 'inquilino'
        case 4: #CONTRATOS
            limpar()
            return 'contratos'
        case 0: #VOLTAR AO MENU ANTERIOR
            limpar()
            print('.......VOLTANDO.......')
        case _: #INVÁLIDO
            limpar()
            print('Não há função correspondente a esse valor!')
        



def escolhe_funcao():

    menus.menu_funcao()
    opcao = int(input('Digite o valor correspondente: '))

    match opcao:
        case 1: #CADASTRAR
            limpar()
            return 'cadastrar'
        case 2: #LISTAR
            limpar()
            return 'listar'
        case 3: #EXCLUIR
            limpar()
            return 'excluir'
        case 4: #EDITAR
            limpar()
            return 'editar'
        case 0: #SAIR
            limpar()
            print('.......SAINDO.......')
            exit()
        case _: #INVÁLIDO
            limpar()
            print('Não há função correspondente a esse valor!')
