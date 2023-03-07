'''
#Criar sua função própria
#Definição de uma nova função
def soma (a,b, c):
    print('Daniel')
    print("$$")
    print(a+b + 20)

soma (2,9, 10)
soma (4,34, 5)
soma (5,7, 11)
soma (1,27, 6)

'''
'''
def pesquise (lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None

L= [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 20))
'''
def soma(L):
    total = 0
    for e in L:
        total+=e
    return total
def média (L):
    return(soma (L)/len(L))
L = [10, 20, 25, 30]
print(soma(L))
print(média(L))


