funcionarios = ["Ana", 'Marcos', 'Alice','Pedro','Sophia','Bruno','Melissa']
Turno_dia = ["Ana", 'Marcos', 'Alice','Melissa']
Turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos', 'Alice','Bruno','Melissa']

lista1 = set(tem_carro)
lista2 = set(Turno_noite)
print (lista1.intersection(lista2))


lista1 = set(tem_carro)
lista5 = set(Turno_dia)
print (lista1.intersection(lista5))



lista6 = set(funcionarios)
lista7 = set(tem_carro)
print (lista6.difference(lista7))