
def soma(*num1):
    resultado = 0
    for num in num1:
        resultado +=num
    return resultado

x= soma(2,4,5,6)
print(x)

def agencia(**carro):
    return carro

print(agencia("Gol","branco",1.0))
