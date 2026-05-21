import config 
import func_calc

while config.ligado == True:
   config.editor = func_calc.simular_botoes(config.editor)
   if config.calcular == True:
      x, config.editor = config.editor, []
      config.editor = func_calc.calculadora(x)
   print(config.editor)