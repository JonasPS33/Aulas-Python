
cidades = ['Fortaleza', 'São paulo' ,'Salvador']
cidades.append("Roma")
cidades.append("ceara")
cidades.append("Nibiru")
cidades.append("Oslo")
#cidades.remove("São paulo")
cidades.insert(1,"coritiba")
cidades.pop(0)
cidades.sort()


print(cidades)

numeros = [1,2,3,4,5]
letras = ['a','b','c','w','t']
numeros.extend(letras)
print(numeros[7])

valores = [50,44,32,24,67]
for x in valores:
    print(f'Esses são os valores r${x}.')


cores = ['amarelo','verde','azul','branco']

if 'rosa' in cores:
    print("sim")
else:
    print("não")


duas_listas = zip(cores,valores)
print(list(duas_listas))


frutas_usuarios = input('Digite o nome das frutas separados por virgulas; ')

frutas_listas = frutas_usuarios.split(',')

print(frutas_listas)
