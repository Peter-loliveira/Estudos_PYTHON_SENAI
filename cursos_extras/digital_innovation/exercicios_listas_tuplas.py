# lista = []
# nome = ''
# while nome != '0':
#     nome = input('Digite o nome do animal: ')
#     lista.append(nome)
#     for x in lista:
#         print(x)

# animal = input('Digite o nome do animal para verificar se o mesmo consta da lista: ')
# if animal in lista:
#     print('{} ja consta da lista.'.format(animal))
# else:
#     print('{} não consta da lista.'.format(animal))

# lista_numerica = []
# x = -1
# while x != 0:
#     x = int(input('Digite um nr para somar aos que já foram digitados: '))
#     lista_numerica.append(x)
#     print(sum(lista_numerica))
# for p in lista_numerica:
#     print(p)

# x = int(input('Digit um nr. Se ele constar da lista ele será removido: '))
# if x in lista_numerica:
#     lista_numerica.remove(x)
#     print('Nova lista: {}'.format(lista_numerica))
# lista_numerica.sort()
# print('Nova lista, só que ARRUMADA: {}'.format(lista_numerica))
# lista_numerica.reverse()
# print('Nova lista, só que REVERTIDA: {}'.format(lista_numerica))

tupla = (1,3,2,4,5,7,8,6,0,9)
print(tupla)

tupla = list(tupla)
print(tupla)

tupla.sort()
print(tupla)

tupla.remove(3)
print(tupla)