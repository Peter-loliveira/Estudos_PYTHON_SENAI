""" 
• Escreva um programa que o usuário escolha uma das quatro
opções de lazer noturno:
• 1) Jogar; 2) Assistir seriado; 3) Usar redes sociais; 4) Programar
• Se o usuário escolher as opções 1, 2 ou 3, o programa passa
• Se o usuário escolher 4, o programa informa que detectou uma
mentira e faz uma parada inesperada
• Deve exibir uma mensagem de fim de programa somente quando
tiver uma saída normal do while
•O programa deve repetir o menu até que o usuário digite uma
opção válida

"""

lazeres = '\nEscolha seu lazer preferido:\n1 - Jogar. \n2 - Assistir seriado. \n3 - Usar redes sociais. \n4 - Programar.\n'

opcao = 0
while not opcao in [1,2,3,4]:
    opcao = int(input(lazeres))
    if opcao == 4:
        print('\n#############################\nERRO! ERRO! ERRO! ERRO! ERRO!\n O PROGRAMA SERÁ FINALIZADO\n#############################\n')
        break
    print('\n###############################\n       OK. OPÇÃO VÁLIDA\n OBRIGADO POR SUA PARTICIÁÇÃO\n     E AGORA SE SAIA.\n###############################\n')