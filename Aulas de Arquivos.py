'''
arquivo = open("numeros.txt","w")
for linha in range (1,101):
    arquivo.write("%d\n" % linha)
arquivo.close()

'''
'''
arq = open("Aula.txt","r")

for n in arq.readlines():
    print(n)

arq.close()

'''
arquivo = open("agenda.txt","a")
nome = input('Informe seu nome: ')
email = input('Informe seu e-mail: ')

#for linha in range(1,101):

arquivo.write(f"Nome: {nome}\n Contato: {email}\n")

arquivo.close()