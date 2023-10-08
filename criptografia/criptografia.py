modo = ''
resultado = ''
modo = input("Você deseja:\n1 - criptografar \n2 - descriptografar: ")

if(modo == '1'):
       texto = input("Insira um texto para criptografar: ")

       for i in range (0, len(texto)):
           resultado = resultado + chr(ord(texto[i]) + 1)
           print(resultado)
           resultado = ''

           
if(modo == '2'):
      texto = input("Insira um texto para descriptografar: ")

      for i in range (0, len(texto)):
            resultado = resultado + chr(ord(texto[i]) - 1)
            print(resultado)
            resultado = ''
