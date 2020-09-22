class Banco:
    def __init__( self, nome_banco, ano_fundacao ):
        self.nome = nome_banco
        self.fundacao = ano_fundacao
        self._lista_agencias = []
    
    def adicionar_agencia(self,agencia):
        if agencia not in self._lista_agencias:
            self._lista_agencias.append(agencia)
    
    def listar_agencias(self):
        for agencia in self._lista_agencias:
            print('Agencia:', agencia.numero)
            print(agencia.listar_contas())
        