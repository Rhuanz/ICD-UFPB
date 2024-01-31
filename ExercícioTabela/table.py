'''
Aluno: Rhuan Gabriel do Nascimento Galdino
Matrícula: 20230021591
Descrição: Arquivo de implementação de funções para criação e manipulação de tabela simples
'''
import pandas as pd

def createTable(colunas, dados):

  for linha in dados:

    if len(linha) != len(colunas):

      #print('Falta ou excesso de dados')
      return

  return {colunas[i]:[dados[j][i] for j in range(len(dados))] for i in range(len(colunas))}

#OK
def addLine(table, dados):

  if len(table.keys()) != len(dados):

    #print("Falta ou excesso de dados")
    return table

  else:

    kw = list(table.keys())
    for i in range(len(dados)):

      table[kw[i]].append(dados[i])

    return table

#ok
def removeLine(table, idx):

  try:

    for coluna in table:

      table[coluna].remove(table[coluna][idx])

    return table

  except(IndexError):

    #print("Indice inexistente")
    return table

#OK
def addColum(table, coluna, dados):
  keys = list(table.keys())
  if len(dados) != len(table[keys[0]]):

    #print('Falta ou excesso de dados')
    return table

  else:

    table.update({coluna: dados})
    return table

#OK
def removeColum(table, delColuna):

  if not delColuna in table.keys():

    #print("Coluna inexistente")
    return table

  else:

    ntable = {coluna: table[coluna].copy() for coluna in table if coluna != delColuna}
    return ntable

#OK
def sumColum(table):

  somas = {}
  for coluna in table:

    if type(table[coluna][0]) == int or type(table[coluna][0]) == float:

      somas.update({f'soma {coluna}': sum(table[coluna])})

  return somas

#OK
def meanColum(table):

  media = {}
  for coluna in table:

    if type(table[coluna][0]) == int or type(table[coluna][0]) == float:

      media.update({f'media {coluna}': sum(table[coluna])/len(table[coluna])})

  return media

#ok
def printTable(table):
  try:
    colunas = list(table.keys())
    print(colunas)

    for i in range(len(table[colunas[0]])):

      line = []
      for coluna in colunas:

        line.append(table[coluna][i])

      print(line)
    print() #print pra quebra de linha
  except (AttributeError):
    return


def csvTable(arq):
  try:
    ntable = pd.read_csv(arq+'.csv')
    return createTable(list(ntable.columns), list(ntable.values))
  except (FileNotFoundError):
    #print("Arquivo inexistente")
    return
  
#ok
def filterTable(table, condicao):

  dados = []
  for coluna in table.keys():

    if type(condicao) == int and type(table[coluna][0]) == int or type(condicao) == float and type(table[coluna][0]) == float:

      for i in range(len(table[coluna])):

        if condicao == table[coluna][i]:

          dados.append([table[k][i] for k in table.keys()])

    elif type(condicao) == str and type(table[coluna][0]) == str:

      for item in table[coluna]:

        if condicao.lower() in item.lower():

          idx = table[coluna].index(item)
          dados.append([table[k][idx] for k in table.keys()])

  if not dados:

    #print("nenhum dado encontrado")
    return table

  else: return createTable(list(table.keys()), list(dados))
