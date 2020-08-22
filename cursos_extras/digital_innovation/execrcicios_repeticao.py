# separador = '\n######################\nLAÇO DE REPETIÇÃO  FOR\n######################\n'
# print(separador)

# intervalo = int(input('Entre com um número: '))
# if intervalo <= 0:
#     print('Digite numeros maiores que 0')
# elif intervalo > 2000: 
#     negacao = '\n################################################\nNEM FERRANDO QUE VOU FAZER ESSES CÁLCULOS TODOS!\n################################################\n'
#     print(negacao)
# else:
#     primos = []
#     for x in range(1, intervalo + 1):
#         aux = 0
#         for y in range(1, x+1):
#             if x % y == 0:
#                 aux += 1
#         if aux == 2:
#             primos.append(y)

#     for indice in range(len(primos)):
#         print('{}º número primo: {}'.format(indice + 1, primos[indice]))

# separador = '\n########################\nLAÇO DE REPETIÇÃO  WHILE\n########################\n'
# print(separador)

# x = 'S'
# while x == 'S' or x == 's':
#     x = input( 'Deseja continuar (S/N)? ')

lista = [1,2,3,4,5,6,7,8,9,10]
# print(len(lista))
for x in range(1,len(lista), 3):
    print(x)
