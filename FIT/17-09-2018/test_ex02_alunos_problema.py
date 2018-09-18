# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return 


def test_ex02():
  print ('Alunos problema')
  assert alunos_problema(True, True)    == True
  assert alunos_problema(False, False)  == True
  assert alunos_problema(True, False)   == False
  assert alunos_problema(False, True)   == False

