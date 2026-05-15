editor = []
ligado = True

def simular_botoes():
   
   ### A interface final vai lidar com botões. Por enquanto usaremos inputs numericos para os testes.
   # 0 a 9 = numeros
   # 10 = "="
   # 11 = "+"
   # 12 = "-"
   # 13 = "x"
   # 14 = "/"
   # 15 = apagar

   iu = int(input("Digite: "))
   if iu >= 10:
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
                           return simular_botoes.pop()
                        else:
                            global ligado 
                            ligado = False
                            return 
        
   else:
      return simular_botoes.append(iu)

while ligado == True:
   simular_botoes()
   print(simular_botoes)
