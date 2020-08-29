array_dezenas = {
    '10': 'Dez',
    '11': 'Onze',
    '12': 'Doze',
    '13': 'Treze',
    '14': 'Quatorze',
    '15': 'Quinze',
    '16': 'Dezesseis',
    '17': 'Dezessete',
    '18': 'Dezoito',
    '19': 'Dezenove',
}

dezenas = {
    '2': "vinte",
    '3': "Trinta",
    '4': 'Quarenta',
    '5': "Cinquenta",
    '6': "Sessenta",
    '7': "Setenta",
    '8': "Oitenta",
    '9': "Noventa",
}

unidades = {
    '0': '',
    '1': 'Um',
    '2': 'Dois',
    '3': 'Tres',
    '4': 'Quatro',
    '5': 'Cinco',
    '6': 'Seis',
    '7': 'Sete',
    '8': 'Oito',
    '9': 'Nove'
}

numero = input('Digite um Nr: ')
while numero != '0':
    if numero in array_dezenas:
        print(array_dezenas.get(numero))
    elif len(numero) == 2 and numero[1] == '0':
        print('{}'.format(dezenas[numero[0]]))
    else: 
        print('{} e {}'.format(dezenas[numero[0]], unidades[numero[1]]) if len(numero) == 2 else '{}'.format(unidades[numero[0]]))
    numero = input('Digite um Nr: ')