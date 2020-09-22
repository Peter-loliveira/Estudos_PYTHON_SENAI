class ContaBanco:
    _id = 0

    @property
    def id(cls):
        return cls._id
    @classmethod
    def gera_novo_id_conta(cls, id_ultima_conta):
        cls._id = id_ultima_conta + 1

    def __init__(self, titular, tipo_desejado):
        ContaBanco.gera_novo_id_conta(self.id)
        self.num_conta = self.id
        self.tipo_conta = tipo_desejado
        self.titular = titular
        self._saldo = 0
        self._limite_saque = 1000.00
        # self.tipo_conta = tipo_desejado

    @property
    def tipo_conta(self):
        return self._tipo_conta    
    @tipo_conta.setter
    def tipo_conta(self, tipo):
        tiposAceitos = ['C', 'c','S','s','p','P']
        if tipo not in tiposAceitos:
            self._tipo_conta = tiposAceitos[-1]
        else:
            self._tipo_conta = tipo

    @property
    def num_conta(self):
        return self._num_conta
    @num_conta.setter
    def num_conta(self, numero):
        self._num_conta = numero
    
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

    def sacar(self, valor_do_saque):
        if valor_do_saque > self.saldo:
            print( 'TENTATIVA DE SAQUE MAL SUCESSEDIDA, POIS O SALDO É SUFUCIENTE!' )
        elif valor_do_saque > self.limite_saque:
            print( 'Valor do saque acima do estabelecido!' )
        else:
            self.saldo -= valor_do_saque
