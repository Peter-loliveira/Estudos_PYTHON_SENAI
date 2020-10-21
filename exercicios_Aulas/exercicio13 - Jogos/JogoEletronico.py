from Jogo import jogo

class JogoEletronico(jogo):
    def __init__(self, nome, classificacao_etaria, tipo, preco, categoria, plataforma):
        super().__init__(nome, classificacao_etaria, 0, preco)
        self._categoria = categoria
        self._plataforma = []
        self.dados_jogo

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self,categ):
        self._categoria = categ

    @property
    def plataforma(self):
        return self._plataforma
    @plataforma.setter
    def plataforma(self, plataforma_jogo):
        self._plataforma.append(plataforma_jogo)

    def listar_plataformas():
        return self.plataforma.sort()
