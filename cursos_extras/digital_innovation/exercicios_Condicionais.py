n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

if n1 > n2 and n1 >n3:
    print('o maior valor digitado foi: {}'.format(n1))
elif n2 > n1 and n2 > n3: 
    print('o maior valor digitado foi: {}'.format(n2))
elif n3 > n1 and n3 > n2: 
    print('o maior valor digitado foi: {}'.format(n3))
else: 
    print('Os numeros digitados são iguais')
