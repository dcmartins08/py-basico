a = 10
b = 0
try:
    print(10/4)

except TypeError as error:
    print('tipo errado!!! ')


except ZeroDivisionError as error:
    print('não podi dividi por o' , error)