""" 
Imagine que a pandemia tenha acabado, você recebeu dinheiro e férias para viajar para o exterior e relaxar. Considere os 5 destinos disponíveis, e o preço da viagem por pessoa:
Miami: R$ 5000,00
Barcelona: R$ 6500,00
Florença: R$ 7500,00
Amsterdã: R$ 8500,00
Tóquio: R$ 10000,00
Crie uma lista para armazenar os preços, na mesma ordem indicada acima.
Peça para o usuário informar o destino desejado.
Peça para o usuário informar a quantidade de pessoas da viagem.
Exiba o valor total da viagem.
Exiba se é V ou F que o valor ficou R$12000,00 e R$17000,00.
Exiba se é V ou F que o valor pode ser parcelado em 3x iguais.
Exiba se é V ou F que o destino escolhido fica fora da Europa.
Obs.: Desenvolver o código-fonte preferencialmente sem utilizar estruturas condicionais nem de repetição.

""" ################################################################################################# """


# Listas
destinos = ['Miami', 'Barcelona', 'Florença', 'Amsterdã','Tóquio']
valores = [5000, 6500, 7500, 8500,10000]

# Captura dados do usuário
print('Nossos possives destinos:')
print('Destino 1 -',destinos[0],"${:,.2f}".format(valores[0]))
print('Destino 2 -',destinos[1],"${:,.2f}".format(valores[1]))
print('Destino 3 -',destinos[2],"${:,.2f}".format(valores[2]))
print('Destino 4 -',destinos[3],"${:,.2f}".format(valores[3]))
print('Destino 5 -',destinos[4],"${:,.2f}".format(valores[4]),'\n')
destino = int(input('Favor selecione o destino desejado pelo nr: ')) -1
total_passageiros = int(input('Informe o total de passageiros: '))
total_viagem = valores[destino] * total_passageiros

# Solcitação d
print('Seu destino foi:',destinos[destino])
print('Total de passageiros:', total_passageiros)
print('O valor será de:',"${:,.2f}".format(total_viagem),'\n' )

print('O valor total ficou entre o intervalo de $12.000 e $17.000?')
print('Verdadeiro\n' if total_viagem >= 12000 and total_viagem <= 17000 else 'Falso\n')

print('O valor pode ser dividido em 3x iguais?')
print('Verdadeiro\n' if total_viagem %3 == 0 else 'Falso\n')

print('O destino fica FORA da Europa?')
# quebrei a linha só pra não ficar muito longa
print('Falso' 
if destino == destinos.index('Barcelona') 
or destino == destinos.index('Florença') 
or destino == destinos.index('Amsterdã') 
else 'Verdadeiro')
