rendimento = float(input("Qual o redndimento da lata? "))
altura = float(input("Qual é a altura da parede? "))
largura = float(input("Qual é a largura da parede? "))


def Quantidade_lata():
     area = altura * largura
     latas = area / rendimento 

     print(f"Você precisa de : {latas}")

Quantidade_lata()