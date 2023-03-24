salario = float(input())
reajuste1 = float((salario*15) / 100)
reajuste2 = float((salario*12) / 100)
reajuste3 = float((salario*10) / 100)
reajuste4 = float((salario*7) / 100)
reajuste5 = float((salario*4) / 100)

if salario <= 400.00:
    print("Novo Salário: R$%0.2F"%(salario + reajuste1))

if salario > 400.01 < 800.00:
    print("Novo Salário: R$%0.2F"%(salario + reajuste2))

if salario > 800.01 < 1200.00:
    print("Novo Salário: R$%0.2F"%(salario + reajuste3))

if salario > 1200.01 < 2000.00:
    print("Novo Salário: R$%0.2F"%(salario + reajuste4))

if salario < 2000.00:
    print("Novo Salário: R$%0.2F"%(salario + reajuste5))