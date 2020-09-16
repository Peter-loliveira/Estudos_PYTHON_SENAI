from ContaBanco import ContaBanco

def main():
    c1 = ContaBanco('Peter', 'C')
    print('\nCONTA CRIADA COM SUCESSO!\n')
    c1.depositar(400)
    c1.sacar(1200)
    c1.exibe()

    c2 = ContaBanco('Victor', 'P')
    print('\nCONTA CRIADA COM SUCESSO!\n')
    c2.depositar(1300)
    c2.sacar(900)
    c2.exibe()

    c3 = ContaBanco('Victor', 's')
    print('\nCONTA CRIADA COM SUCESSO!\n')
    c3.depositar(1300)
    c3.sacar(900)
    c3.exibe()

main()
