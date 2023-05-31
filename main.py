import usarchatgpt as gpt

produtos = ['celular xiaomi lite 9', 'celta lt', 'ar condicionado lg']

resposta = gpt.consultarchatgpt(produtos[0])

print(resposta)