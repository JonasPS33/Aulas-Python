
list1 = [10,20,40 ,50,60]
list2 = [10,20,30,70,80]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)
print(num1 ^ num2)
print(num1 & num2)
print(num1 - num2)

num1.add(120)
num1.remove(60)


print(num1)

alfabeto = {'a','b','c','d'}
alfa = {'a','j','h'}

alfa1 = alfabeto.intersection(alfa)

print(alfa1)



