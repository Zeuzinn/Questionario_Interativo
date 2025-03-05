cadastro = {'Nome': ''}
perguntas =[
    {
        'Pergunta' : 'Qual fruta é geralmente vermelha e redonda?',
        'Opção': ['Banana', 'Laranja', 'Maçã', 'Uva'],
        'Resposta' : 'Maçã',
    },
    {
        'Pergunta': 'Quantas vogais tem a palavra "CADEIRA"',
        'Opção': ['3', '2', '4', '6'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Qual destes animais faz "MIAU"',
        'Opção': ['Pato', 'Gato', 'Leão', 'Macaco'],
        'Resposta': 'Gato',
    },
    {
        'Pergunta': 'Qual é o primeiro mês do ano?',
        'Opção': ['Dezembro', 'Fevereiro', 'Abril', 'Janeiro'],
        'Resposta': 'Janeiro',
    },
    {
        'Pergunta': 'Quantos dedos temos em uma mão?',
        'Opção': ['5', '4', '6', '20'],
        'Resposta': '5',
    },
    
]
pergunta_certa=2
qtd_acertos=0
n=0

nome=input('Nome do aluno: ')
cadastro['Nome']= nome
print(cadastro)
login=input('Nome: ')

if login == cadastro['Nome']:
    print('Acesso Liberado')
else:
    print('Acesso negado')
for pergunta in perguntas:
    n+=1
    print(f'Questão {n}:',pergunta['Pergunta'])
    print()
        
    opcoes = pergunta ['Opção']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
        
    print()
    resposta= input('Resposta: ')
    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
        
    if acertou:
        qtd_acertos+=1
        print('Acertou 👍')
    else:
        print('Errou ❌')

print('Você acertou', qtd_acertos,'de', len(perguntas), 'perguntas.')
media = qtd_acertos * pergunta_certa
print(f'Média: {media}')

if media > 5:
    print()
    print(f'Com a média:{media} o(a) aluno(a) {cadastro["Nome"]} está APROVADO')
else:
    print()
    print(f'Com a média:{media} o(a) aluno(a) {cadastro["Nome"]} está REPROVADO!')