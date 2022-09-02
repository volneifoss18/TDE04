contaBancaria = float(input('Qual o número da sua conta bancária? '))
saldo = float(input('Qual o saldo da sua conta bancária? '))
 
if saldo >= 0:
    print('CONTA NORMAL.')
else:
    print('CONTA ESTOURADA')
