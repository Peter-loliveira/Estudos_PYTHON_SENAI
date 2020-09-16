from ContaBanco import ContaBanco

def main():
    c1 = ContaBanco('Peter', '')
    c1.tipo_conta = 'P'
    print('\nCONTA CRIADA COM SUCESSO!\n')
    c1.depositar(400)
    c1.sacar(1200)
    c1.gera_novo_id_conta(c1.id)
    c1.exibe()
   
    c2 = ContaBanco('Victor', '')
    
    c2.tipo_conta = 't'
    print('CONTA CRIADA COM SUCESSO!')
    c2.depositar(1300)
    c2.sacar(900)
    c2.gera_novo_id_conta(c2.id)
    c2.exibe()

main()
