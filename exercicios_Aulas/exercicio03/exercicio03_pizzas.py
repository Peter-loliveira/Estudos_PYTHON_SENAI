texto = '\nInforme o que achou de Python\n1 - MUITO BARRIL.\n2 - BARRIL.\n3 - MARROM MENOS.\n4 - DE BOA.\n5 - MUITO DE BOA\n'
conjunto = [1,2,3,4,5]

x = int(input(texto))
while not (x in conjunto) or (x == 0):
    print('\n######################################\nNota fora dos parametros apresentados. \n       Favor digitar novamente.\n######################################\n')
    x = int(input(texto))
    x in conjunto
    if x == 0:
        print('\n###################\n  VOCÊ TÁMALUCO!\nNO PIZZA FOR YOU!!!\n###################\n')
        break
else:
    if x in [1,2]:
        print('\n##################################\nPor sua nota,você ganha UMA pizza!\n##################################\n')
    elif x in [3,4]:
        print('\n###################################\nPor sua nota,você ganha DUAS pizza!\n###################################\n')
    elif x == 5:
        print('\n###################################\nPor sua nota,você ganha TRÊS pizza!\n###################################\n')