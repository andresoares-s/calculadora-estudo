import config
def simular_botoes(x):
   
   ### A interface final vai lidar com botões. Por enquanto usaremos inputs numericos para os testes.
   # 0 a 9 = numeros
   # 10 = "="
   # 11 = "+"
   # 12 = "-"
   # 13 = "x"
   # 14 = "/"
   # 15 = apagar
   iu = int(input("Digite: "))
   if iu >= 10 or iu < 0:
    if iu == 10:
       return 
    else: 
        if iu == 11:
           return 
        else:
            if iu == 12:
               return 
            else:
                if iu == 13:
                   return 
                else:
                    if iu == 14:
                       return 
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