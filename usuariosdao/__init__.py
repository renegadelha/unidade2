def validar_login(dicio, login, senha):
    achei = False

    for i in dicio:
        if (i == login):
            password = dicio[login][0]
            if (password == senha):
                achei = True

    return achei

def cadastrar_usuario(dicion):
    login = input('digite o login para cadastrar')
    senha = input('digite a senha para cadastrar')
    nome_compl = input('digite seu nome completo')
    cpf = input('digite seu cpf')

    # verificar se este login já está cadastrado
    dicion[login] = [senha, nome_compl, cpf, []]
