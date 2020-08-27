""" 
Crie uma lista com 6 temperaturas: 33.5, 28.7, 36.1, 30.9, 35.3,
27.0
• Percorra todas as temperaturas da lista
• Caso a temperatura seja maior ou igual a 35 graus, mostre uma
mensagem que a temperatura é muito quente
• Se a temperatura for menor do que 35 graus e maior ou igual a 30,
mostre uma mensagem que a temperatura é quente
• Do contrário, mostre uma mensagem que a temperatura é amena
"""

temps = [33.5, 28.7, 36.1, 30.9, 35.3,27.0]
print('\n#############################')
for tempAtual in range(len(temps)):
    print('{}. TEMPERATURA MUITO ALTA!'.format(temps[tempAtual]) if temps[tempAtual] >= 35 else '{}. TEMPERATURA AMENA!'.format(temps[tempAtual]))
print('#############################\n')