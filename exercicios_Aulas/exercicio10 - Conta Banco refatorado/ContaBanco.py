class ContaBanco:
    _id = 0

    @property
    def id(cls):
        return cls._id
    @classmethod
    def gera_novo_id_conta(cls, id_ultima_conta):
        cls._id = id_ultima_conta + 1

    def __init__(self, titular, tipo_desejado):
        self.titular = titular
        self._tipo_conta = ''
        self._num_conta = ''
        self._saldo = 0
        self._limite_saque = 1000.00

        @property
        def id(cls):
            return cls._id
        @id.setter
        def id(cls,contaID):
            self._id = atualiza_Contas(cls.id)

    @property
    def num_conta(self):
        return self._num_conta
    @num_conta.setter
    def num_conta(self, numero_da_conta):
        self._num_conta = numero_da_conta
        
    @property
    def tipo_conta(self):
        return self._tipo_conta    
    @tipo_conta.setter
    def tipo_conta(self, tipo_da_conta):
        tiposAceitos = ['c', 'C', 'p','P']
        if tipo_da_conta not in tiposAceitos:
            print( 'Tipo não compativel. A conta será setada para POUPANÇA (P)' )
            self._tipo_conta = tiposAceitos[-1]
        else:
            self._tipo_conta = tipo_da_conta

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, novo_valor):
        self._saldo = novo_valor
    
    @property
    def limite_saque(self):
        return self._limite_saque
    @limite_saque.setter
    def limite_saque(self,novo_limite):
        self._limite_saque = novo_limite

    def depositar(self, valor_do_deposito):
        self.saldo += valor_do_deposito
        print( 'Realizado deposito de R$', valor_do_deposito )

    def sacar(self, valor_do_saque):
        if valor_do_saque > self.saldo:
            print( 'TENTATIVA DE SAQUE MAL SUCESSEDIDA, POIS O SALDO É SUFUCIENTE!' )
        elif valor_do_saque > self.limite_saque:
            print( 'Valor do saque acima do estabelecido!' )
        else:
            self.saldo -= valor_do_saque
            print( 'Realizado saque de R$', valor_do_saque )
    
    def exibe(self):
        print('--------------------------------------------------')
        print( 'Numero da conta:', self._id, '| Titular:', self.titular, '| Tipo Conta:', self.tipo_conta )
        print( 'Limite de Saque: ', self.limite_saque)
        print( 'Saldo:', self.saldo,)
        print('--------------------------------------------------')
        print( '\n' )
