

lista1 = [1,2,3,4,44,6]

#def multi(x):
    #return x * 2

lista2 = map(lambda x: x*2,lista1)


print(list(lista2))

def remover20(x):
    return x > 20

print(list(filter(remover20,lista1)))


