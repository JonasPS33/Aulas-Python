
try:
  letras =["a",'b',"c"]
  print(letras[3])
except IndexError:
  print("Index não existe")

try:
 valor = int(input("Digite o valor do seu produto: "))
 print(valor)
except ValueError:
  print("Digite o valor em numeros")