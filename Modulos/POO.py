from datetime import datetime


# Criar classe
class Funcionarios:
   def __init__(self,nome,sobrenome,ano_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.ano_nascimento = ano_nascimento
   def nome_completo(self):
      return self.nome + ' ' + self.sobrenome
   def idade_funcionario(self):
       ano_atual = datetime.now().year
       self.ano_nascimento = int(ano_atual - self.ano_nascimento)
       return self.ano_nascimento
       
#criar objeto
usuario1 = Funcionarios("Naty", "silva", 1999)
usuario2 = Funcionarios('Jonas','Pinheiro',2000)
usuario3 = Funcionarios('tay','ers',2004)


print(Funcionarios.idade_funcionario(usuario1))

print(Funcionarios.idade_funcionario(usuario3))

print(Funcionarios.idade_funcionario(usuario2))
#print(Funcionarios.nome_completo(usuario2))
#print(Funcionarios.nome_completo(usuario3))


#Criar parametros
#usuario1.data_nascimento = "12/01/2009"
#usuario1.nome = 'naty'
#usuario1.sobrenome = 'Lima'

#usuario2.data_nascimento = "12/01/1088"
#usuario2.nome = 'jonas'
#usuario2.sobrenome = 'solva'
