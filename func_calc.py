import config
def simular_botoes(x):
   """ A interface final vai lidar com botões. Por enquanto usaremos inputs numericos para os testes.
   0 a 9 = numeros
   10 = "="
   11 = "+"
   12 = "-"
   13 = "x"
   14 = "/"
   15 = apagar
   """
   iu = int(input("Digite: "))
   if iu >= 10 or iu < 0:
    if iu == 10:
       concatenado = concatenar(config.editor)
       print(concatenado)
       config.calcular = True
       x = calculadora(concatenado)
       return x
    else: 
        if iu == 11:
           if type(x[len(x)-1]) == int:
              x.append(soma)
              return x
           else: 
              return x      
        else:
            if iu == 12:
               if type(x[len(x)-1]) == int:
                  x.append(sub) 
               return x
            else:
                if iu == 13:
                   if type(x[len(x)-1]) == int:
                      x.append(mul)
                   return x
                else:
                    if iu == 14:
                        return x
                    else:
                        if iu == 15:
                           if not x:
                              return x
                           else:
                              x.pop()
                              return x
                        else:
                           config.ligado = False
                           return       
   else:
      x.append(iu)
      return x
def concatenar(expressao):
   """quando o usuario apertar o igual, o algoritmo vai ler a lista inteira e concatenar os números entre operadores"""
   i = 0
   conc = []
   a = expressao
   contador = len(a)
   if any(type(item) != int for item in a):
      while i <= contador-1:
         conc.append(a[i])
         if type(conc[i]) != int:
            conc.pop()
            operando = int("".join(map(str,conc)))
            editormenos = a[i+1:]
            operador = a[i]
            editornovo = [operando,operador] + concatenar(editormenos)
            return editornovo
         else:   
            i += 1
   else:
      return [int("".join(map(str,a)))]
def calculadora(equacao): 
   if equacao[-1] == soma:
      equacao.append(0)
   elif equacao[-1] == sub:
      equacao.append(0)
   elif equacao[-1] == mul:
      equacao.append(1)
   elif equacao[-1] == div:
      equacao.append(1) 
   i2 = 0
   while i2 < len(equacao):
      if equacao[i2] == mul or equacao[i2] == div:
         if equacao[i2] == mul:
            multemp = mul(equacao[i2 - 1],equacao[i2 + 1])
            equacao = equacao[0:i2 - 1] + [multemp] + equacao[i2 + 2:]
            i2 -= 1
         elif equacao[i2] == div:
            divtemp = div(equacao[i2 - 1],equacao[i2 + 1])
            equacao = equacao[0:i2 - 1] + [divtemp] + equacao[i2 + 2:]
            i2 -= 1
      else: 
         i2 +=1
   i2 = 0
   while i2 < len(equacao):
      if equacao[i2] == soma or equacao[i2] == sub:
         if equacao[i2] == soma:
            sumtemp = soma(equacao[i2 - 1], equacao[i2 + 1])
            equacao = equacao[0:i2 - 1] + [sumtemp] + equacao[i2 + 2:]
            i2 -= 1
         elif equacao[i2] == sub:
            subtemp = sub(equacao[i2 - 1],equacao[i2 + 1])
            equacao = equacao[0:i2 - 1] + [subtemp] + equacao[i2 + 2:]
            i2 -= 1
      else: 
         i2 +=1
   config.calcular = False
   return equacao
def mul(a,b):
   return a*b
def div(a,b):
   return a/b
def sub(a,b):
   return a-b
def soma(a,b):
   return a+b