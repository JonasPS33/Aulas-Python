ponto = int(input("Qual é a temperatura da carne? "))

if ponto < 48 :

    print("A carne deve cozinhar mais!")

elif ponto >= 48 and ponto < 54 :
    print("Selada")

elif ponto >= 54 and ponto < 60 :
    print("Ao ponto mal passada")

elif ponto >= 60 and ponto < 65 :
    print("ao ponto")

elif ponto >= 65 and ponto < 71 :
    print("B]Ao ponto bem passada")

elif ponto >= 71 :
    print("Bem passada")