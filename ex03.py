numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 > numero2:
    sobra = numero1 - numero2
    print(f"O resto de {numero1} - {numero2} é: {sobra}")
elif numero2 > numero1:
    sobra = numero2 - numero1
    print(f"O resto de {numero2} - {numero1} é: {sobra}")