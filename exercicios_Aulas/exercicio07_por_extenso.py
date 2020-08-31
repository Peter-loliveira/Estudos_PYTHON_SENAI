# JEITO NORMAL
array_dezenas = {'10': 'Dez','11': 'Onze','12': 'Doze','13': 'Treze','14': 'Quatorze','15': 'Quinze','16': 'Dezesseis','17': 'Dezessete','18': 'Dezoito','19': 'Dezenove',}

dezenas = {
'2': 'vinte','3': 'Trinta','4': 'Quarenta','5': 'Cinquenta','6': 'Sessenta','7': 'Setenta','8': 'Oitenta','9': 'Noventa',}

unidades = {
'0': '','1': 'Um','2': 'Dois','3': 'Tres','4': 'Quatro','5': 'Cinco','6': 'Seis','7': 'Sete','8': 'Oito','9': 'Nove'}

numero = input('Digite um Nr: ')
while numero != '0':
    if numero in array_dezenas:
        print(array_dezenas.get(numero))
    elif len(numero) == 2 and numero[1] == '0':
        print('{}'.format(dezenas[numero[0]]))
    else: 
        print('{} e {}'.format(dezenas[numero[0]], unidades[numero[1]]) if len(numero) == 2 else '{}'.format(unidades[numero[0]]))
    numero = input('Digite um Nr: ')

# Jeito com MENOS LINHAS, MAS BURRO
# lista = {1:'um',2:'dois',3:'três',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove',10:'dez',11:'onze',12:'doze',13:'treze',14:'quatorze',15:'quinze',16:'dezesseis',17:'dezessete',18:'dezoito',19:'dezenove',20:'vinte',21:'vinte e um',22:'vinte e dois',23:'vinte e três',24:'vinte e quatro',25:'vinte e cinco',26:'vinte e seis',27:'vinte e sete',28:'vinte e oito',29:'vinte e nove',30:'trinta',31:'trinta e um',32:'trinta e dois',33:'trinta e três',34:'trinta e quatro',35:'trinta e cinco',36:'trinta e seis',37:'trinta e sete',38:'trinta e oito',39:'trinta e nove',40:'quarenta',41:'quarenta e um',42:'quarenta e dois',43:'quarenta e três',44:'quarenta e quatro',45:'quarenta e cinco',46:'quarenta e seis',47:'quarenta e sete',48:'quarenta e oito',49:'quarenta e nove',50:'cinquenta',51:'cinquenta e um',52:'cinquenta e dois',53:'cinquenta e três',54:'cinquenta e quatro',55:'cinquenta e cinco',56:'cinquenta e seis',57:'cinquenta e sete',58:'cinquenta e oito',59:'cinquenta e nove',60:'sessenta',61:'sessenta e um',62:'sessenta e dois',63:'sessenta e três',64:'sessenta e quatro',65:'sessenta e cinco',66:'sessenta e seis',67:'sessenta e sete',68:'sessenta e oito',69:'sessenta e nove',70:'setenta',71:'setenta e um',72:'setenta e dois',73:'setenta e três',74:'setenta e quatro',75:'setenta e cinco',76:'setenta e seis',77:'setenta e sete',78:'setenta e oito',79:'setenta e nove',80:'oitenta',81:'oitenta e um',82:'oitenta e dois',83:'oitenta e três',84:'oitenta e quatro',85:'oitenta e cinco',86:'oitenta e seis',87:'oitenta e sete',88:'oitenta e oito',89:'oitenta e nove',90:'noventa',91:'noventa e um',92:'noventa e dois',93:'noventa e três',94:'noventa e quatro',95:'noventa e cinco',96:'noventa e seis',97:'noventa e sete',98:'noventa e oito',99:'noventa e nove'}

# try:
#     numero = int(input('Digite Um Numerodo de 1 a 99: '))
# except:
#     print('Ô Jumento, Isso n~eo é um numero')
# else:
#     print('Numero fora do range' if 0 < numero < 100 else  print(lista.get(numero)))

# Jeito com MENOS LINHAS AINDA E IGNORANDO POSSIBILIDADE DE ERRO DO USUÁRIO, MAS AINDA ASSIM BURRO.

# print(lista.get(int(input('Digite um Numero de 1 a 99: '))))