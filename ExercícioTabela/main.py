'''
Aluno: Rhuan Gabriel do Nascimento Galdino
Matrícula: 20230021591
Descrição: Arquivo para testar funções de criação e manipulação de tabela simples
'''

from table import *

teste = createTable(['nome', 'idade'], [['rhuan', 23], ['Ana', 26]])
printTable(teste)

printTable(addLine(teste, ['gabi', 26]))

printTable(removeLine(teste, 3))

printTable(removeLine(teste, 2))

printTable(addColum(teste, 'sexo', ['Masculino', 'Feminino']))

printTable(removeColum(teste, 'pendrive'))

printTable(removeColum(teste, 'sexo'))

print(sumColum(teste))

print(meanColum(teste))
print()

printTable(filterTable(teste, 25))

teste2 = csvTable('email')
printTable(teste2)