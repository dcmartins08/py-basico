"""
Tabela = {"alface":0.45,"batata":1.20,"tomate":0.45,"feijão":1.50}

print(Tabela)
print(Tabela["feijão"])

Tabela["milho"] = 10
print(Tabela)

print('//'*30)

comida = {"alface":0.45,"milho": 10}

valor = input('informe o nome da comida:')

if valor in comida:
    print(comida[valor])
else:
    print("item não encontrado!!\n")

print(comida.keys())
print(comida.values())

comida = {'alface':10 , 'milho':20}
valores = comida.values()
print(sum(valores))

print('//'*30)

frutas = {"banana": 2, "maça": 3, "laranja": 1}
for chave, valor in frutas.items():
    print (chave, "->", valor)

"""
"""
Alunos = {"Daniel": 42, "Tiago": 45, "Rafael": 78, "Carlos": 92}
print(Alunos)

idade = Alunos.values() 
print(sum(idade))

"""
"""
dic = dict()

for i in range(3):
    chave = input('nome do produto:')
    valor = input('valor do produto:')
    dic[chave] = valor

print(dic)

"""
"""
funcionarios = {'daniel': 440, 'douglas': 696, 'frederico': 104, 'gustavo': 841 }

while True:
    colaborador = input('digite o registro do colaborador, fim pra terminar:')
    if colaborador == 'fim':
        break
    if colaborador in funcionarios:
        print('registro', funcionarios[colaborador])
    else:
        print('colaborador não encontrado no registro!')

"""

"""

                       # Exercício #
# Crie um dicionário que simule um estoque para os seguintes produtos 
# após as criação faça os seguintes passos:
# 1- delete o registro 'mouse' de seu dicionário
# 2- Adicione o produto notebook com 10 unidades no seu dicionário
# 3- Subtraia -1 da quantidade do produto fone

estoque = {'fone': 5, 'tv': 2, 'teclado': 6, 'mouse': 0}

del estoque['mouse']

estoque['notebook'] = 10

estoque['fone'] = 4

print (estoque)

"""

"""
idade = {'daniel': 4002, 'douglas': 555, 'cleiton': 60}

print (  max(idade.values() ) )

"""

alunos = {}

for i in range(2):
    Nome = input('nome:')
    media = float(input('media:'))

    if media >= 7:
        situacao = 'aprovado'
    else: 
        situacao = 'reprovado'

    alunos[Nome] = situacao

print(alunos)