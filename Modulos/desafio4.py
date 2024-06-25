'''def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n -1)

num = int(input("Diigte numero: "))
print(f"O fatorial de {num}  é  {fatorial(num)}")'''

'''def dobro(n):
    return n * 2

def quadrado(q):
    return q**2

print(quadrado(dobro(2))

num = int(input("digite um numero: "))
num2 = lambda x: 'Par' if x % 2 == 0  else 'Impar'  
print(f"O Numero é  {num2(num)}")'''

lista = [1,2,3,4,5,6]
for x in lista:
    lista1 = lambda y: x**2
    print(lista1(lista))
print(type(lista1))



