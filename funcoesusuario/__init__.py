import openai

def consultarchatgpt(produto):
    openai.api_key = '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'

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'me diga resumidamente o que você acha do ' + produto + ' ?'
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text


def menu_principal():
    print('\n-------------BEM VINDO!--------------')
    print('1-Cadastrar vendedor')
    print('2-Fazer login')
    print('3-Sair')
    op = int(input('O que voce deseja fazer?: '))
    return op

def validar_senha(login, senha):
    while login == senha:
        print('Error: a senha não pode ser igual ao login!')
        senha = input('crie sua senha novamente: ')

    return senha

def logar(login, senha, vendedores):

    for dados in vendedores:
        if dados[0] == login and dados[1] == senha:
            print('login feito com sucesso. Bem vindo!')

            return True
    return False

def menu_produto():
    print('\n------------MENU--------------')
    print('1-atualizar senha/informaçoes pessoais')
    print('2-Cadastrar produto')
    print('3-Remover produto')
    print('4-Buscar produto')
    print('5-Atualizar produto')
    print("6-Deslogar")
    return int(input('O que voce deseja fazer?: '))
