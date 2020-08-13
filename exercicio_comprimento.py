tamanho_piso = .25

sala_cump = float(input('SALA: Informa o COMPIMENTO:\n'))
sala_larg = float(input('SALA: Informa o LARGURA:\n'))
sala_area = sala_cump * sala_larg
print('A SALA tem', format(sala_area, ".2f"), 'm2' )
print('Serão gastos R$', format(sala_area * 30, ".2f") , 'para aplicar piso na SALA')
print('Serão necessário', format(sala_area /tamanho_piso, ".2f"), 'pisos para preencher a SALA')
print('\n')

quarto_cump = float(input('QUARTO: Informa o COMPIMENTO:\n'))
quarto_larg = float(input('QUARTO: Informa o LARGURA:\n'))
quarto_area = quarto_cump * quarto_larg
print('O QUARTO tem', format(quarto_area, ".2f"), 'm2' )
print('Serão gastos R$', format( sala_area * 30, ".2f"), 'para aplicar piso no QUARTO')
print('Serão necessário', format(sala_area / tamanho_piso, ".2f"), 'pisos para preencher o QUARTO')
print('\n')

if sala_area != quarto_area:
    print('As áreas dos comodos são DIFERENTES\n')
else:
    print('A área dos comodos são IGUAIS\n')    

if (sala_area + quarto_area) < 50:
    print('A soma das áreas é MENOR que 50 m2\n')
else:
    print('A soma das áreas é MAIOR que 50 m2\n')
    
if sala_area * 30 > 1000 and quarto_area * 30 >1000:
    print('Em UM dos comodos serão gastos mais de R$ 1.000,00')
else:    
    print('Em NENHUM dos comodos serão gastos mais de R$ 1.000,00')

if sala_area / tamanho_piso >= 100 or quarto_area / tamanho_piso >= 100:
    print('Em pe3
    lo menos UM dos comodos serão gastos MAIS que 100 pisos')
else: 
    print('Em NENHUM dos comodos serão gastos MAIS que 100 pisos')

print('\n')