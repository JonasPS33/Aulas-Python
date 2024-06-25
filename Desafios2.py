'''idade = int(input("Digite sua idade: "))

if idade < 13 :
    print(f'Você é uma criança')
elif idade >= 13 and idade <= 19:
     print("Você é um adolescente")
else:
     print("Vpcê é adulto")'''

'''carro = input("Diigte o modelo do seu BMW: ")
carro = carro.upper()

BMW = ["BMW X6","BMW I5",'BMW I8']

if carro in BMW:
    print("Este carro está diponibvel")
else:
    print("Este carro não está disponivel")'''

'''while True:
    fruta = input ("Digite uma fruta: ")
    if fruta == "abacate":
        print("Parabens vc acertou a fruta")
        break'''

#lista = [1,2,3,4,5,6,7,8,9,10]
'''lista = list(range(1,11))
for x in lista:
    if x % 2 == 0:
        print(f"O numero {x} é par ")
    elif x % 2 !=0:
        print(f"Os numero {x} é impar")



Pais = input("Digite o nome de um País: ")
Capital = {'Itália':"Roma",'Brasil':"Rio de Janeiro", 'Noruega':"Oslo"}

if Pais in Capital:
    print(f"A Capital de {Pais} é {Capital[Pais]}: ")

else:
    print("Desculpa não temos informação sobre o pais: "'''

conj = {1,4,6,7,89,8}
conj2 = {3,5,6,8,89,00}

inter = conj2.union(conj)

print(inter)
