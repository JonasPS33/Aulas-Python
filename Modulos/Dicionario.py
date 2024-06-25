aluno = {"nome": 'Jonas',
'idade': 36,
'nota_final': 'A',
'Aprovação': True,
'materias':['ciencia','matematica','portugues']}
aluno.update({'nome':'ana'})
aluno.update({'nome':'jonas'})
print(aluno['nome'])

for x in aluno.values():
    print(x)

