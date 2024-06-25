from Modulos.Funções import find_index
from Modulos.POO import Funcionarios

list1 = ["a","b","c","d","e"]

var1 = find_index(list1,"e")
print(var1)


usuario1 = Funcionarios("Naty", "silva", 1999)
print(Funcionarios.idade_funcionario(usuario1))
