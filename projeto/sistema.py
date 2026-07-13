import uteis 
import proprietario

while True:

    funcao = uteis.escolhe_funcao()
    instituto = uteis.escolhe_instituto()
    
    match instituto:
        case 'proprietario':
            proprietario.execute(funcao)




