numero = int(input('Digite um número: '))

if numero % 2 == 0 and numero > 0:
    print('este número é par e positivo') 
elif numero % 2 == 0 and numero < 0:
        print('este núemro e par e negativo') 
elif numero % 2 != 0 and numero > 0:
        print('este numero e impar e positivo')
else:
    print('este numero é impar e negativo')