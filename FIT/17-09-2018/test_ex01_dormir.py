# Exercícios by Nick Parlante (CodingBat)

# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):

  if (dia_semana == feriado):
      return True

  elif(dia_semana == False) and (feriado == True):
      return True

  else:
      return False

def test_ex01():
  print ('Oba! Hoje vou ficar dormindo!')
  assert dormir(False , False)  == True
  assert dormir(True  , False)  == False
  assert dormir(False , True)   == True
  assert dormir(True  , True)   == True