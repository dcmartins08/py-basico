'''
# EXERCICÍO DE IF(SE) e INDENTAÇÃO

idade = 17     

if idade < 18:

    print ("menor de idade")
    print ("menor de idade")
    print ("menor de idade")

if idade < 19:
    print ("menor de idade222")
    print ("menor de idade222")
    print ("menor de idade222")

print ("fim")


a = int(input (" primeiro valor: "))
b = int(input (" segundo valor: "))

if a > b:
    print ("o primeiro número é o maior!")

if b > a:
    print("o segurdo número é o maior!")



# estrutura de aninhadas de blocos

minutos = int(input (" quantos minutos você utilizou este mês: "))
if minutos < 200:
   preço = 0.20 

else:

    if minutos < 400:
        preço = 0.18
 
    else:

        preço = 0.15


print (preço)

'''

# EXEMPLO DE (ELIF)

categoria = int(input(" digite a categoria do produto: "))
if categoria  == 1:
    preço = 10

elif categoria == 2:
    preço = 18 

elif categoria == 3:
    preço = 23

elif categoria == 4:
    preço = 26

elif categoria == 5:
    preço = 31

else:
    print (" categoria invalida, digite um valor entre 1 e 5! ")
    preço = 0

print ( preço )