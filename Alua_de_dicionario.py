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

dic = dict()

for i in range(3):
    chave = input('nome do produto:')
    valor = input('valor do produto:')
    dic[chave] = valor

print(dic)


