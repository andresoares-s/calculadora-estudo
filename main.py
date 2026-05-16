import config 
from func_calc import simular_botoes
editor = []

while config.ligado == True:
   editor = simular_botoes(editor)
   print(editor)