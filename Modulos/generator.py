from sys import getsizeof


valores = [x*10 for x in range(6)]
print(valores)
print(type(valores))
print(getsizeof(valores))


valores = (x*10 for x in range(6))
print(valores)
print(type(valores))
print(getsizeof(valores))