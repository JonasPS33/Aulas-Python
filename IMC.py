altura = float(input("Qual é a sua altura: "))
peso = float(input("Qual é o seu peso: ") )
IMC = peso / (altura/100) **2

print(f"Seu IMC é {IMC:,.2f}")

if IMC < 18.5:
    print("Magreza")

elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")

elif IMC >= 25 and IMC <= 29.9:
    print("sobrepeso")

elif IMC >= 30 and IMC <= 39.9:
    print("Obesidade")

elif IMC >= 40:
    print("Obesidadde grave")