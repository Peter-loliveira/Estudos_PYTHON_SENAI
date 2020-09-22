from ContaBanco import ContaBanco

def main():
    # Criei mais um tipo de conta afim de dar ter mais uma opção para testar
    # TIPOS DE CONTA: C = Corrente; P = poupança e S = Salário
    
    c1 = ContaBanco('Peter', 'C')
    print('CONTA CRIADA COM SUCESSO!')
    c1.depositar(400)
    c1.sacar(1200)
    c1.exibe()

    c2 = ContaBanco('Victor', 'P')
    print('CONTA CRIADA COM SUCESSO!')
    c2.depositar(1300)
    c2.sacar(900)
    c2.exibe()

    c3 = ContaBanco('Victor', 'K')
    print('CONTA CRIADA COM SUCESSO!')
    c3.depositar(1300)
    c3.sacar(900)
    c3.exibe()

main()
