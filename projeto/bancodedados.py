proprietario = []
imoveis = []
inquilinos = []
contratos = []

id_proprietario = 1
id_imovel = 1
id_inquilino = 1
id_contrato = 1


novo_proprietario = {

    "id" : None,
    "nome" : None,
    "cpf" : None,
    "imoveis" : []
    
}

novo_imovel = {

    "id" : None,
    "endereco" : None,
    "valor" : None,
    "tipo" : None

}

novo_inquilino = {

    "id" : None,
    "nome" : None,
    "cpf" : None,
    "id_imovel" : None,
    "imovel" : None,
    "id_proprietario" : None,
    "proprietario" : None

}

novo_contrato = {

    "id" : None,
    "inquilino" : None,
    "proprietario" : None,
    "imovel" : None,
    "valor" : None,
    "data_inicio" : None,
    "data_termino" : None

}


