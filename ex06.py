from math import sqrt
 
 
num1 = float(input('Digite um número '))
num2 = float(input('Digite mais um número '))
num3 = float(input('Digite apenas mais um número '))
quadrado = num1 ** 2
intervalo = ('NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO')
diferenca = (num2 - num3)
diferenca2 = (num3 + num2)
 
if num1 > 0:
    raiz = sqrt(num1)
    print(f'Seu numero é positivo, portanto sua raiz é {raiz}')
else:
    print(f'Seu número é negativo, portanto o seu quadrado é {quadrado}')
if num2 > 10 and num2 < 100:
    print(intervalo)
else:
    print('Seu número não está no intervalo permitido de 10 a 100.')
if num3 < num2:
    print(f'Seu terceiro número é menor que o segundo, portanto sua diferença é de {diferenca}')
else:
    print(f'Seu terceiro número é maior que o segundo, portanto sua soma é de {diferenca2}')
