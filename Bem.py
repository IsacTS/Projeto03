import locale
import textwrap
try:
    locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')
except locale.Error:
    pass
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    pass
try:
    locale.setlocale(locale.LC_ALL, 'pt')
except locale.Error:
    pass


class Bem:
    def __init__(self, cod_tipo, desc_tipo, descricao, valor):
        assert type(cod_tipo) is int, "cod_tipo tem de ser um inteiro: {}".format(type(cod_tipo))
        assert type(valor) is float, "valor tem de ser numerico: {}".format(type(valor))
        self.__cod_tipo = cod_tipo
        self.__desc_tipo = desc_tipo
        self.__descricao = descricao
        self.__valor = valor

    def __str__(self):
        valor = locale.currency(self.valor, grouping=True, symbol=False)
        saida = "{0} -- {1} -- R${2}\n".format(self.cod_tipo, self.desc_tipo, valor)
        saida += textwrap.fill("Descricao: {}\n".format(self.descricacao), 80)
        return saida

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Bem):
            return False
        return self.valor == other.valor and self.descricao == other.descricao

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        assert isinstance(other, Bem), "other nao e' do tipo Bem: {}".format(type(other))
        if self.valor < other.valor:
            return True
        elif self.valor == other.valor:
            if self.cod_tipo < other.cod_tipo:
                return True
            elif self.cod_tipo == other.cod_tipo:
                return self.descricao < other.descricao
        return False

    def __le__(self, other):
        assert isinstance(other, Bem), "other nao e' do tipo Bem: {}".format(type(other))
        return self.valor <= other.valor

    def __gt__(self, other):
        assert isinstance(other, Bem), "other nao e' do tipo Bem: {}".format(type(other))
        if self.valor > other.valor:
            return True
        elif self.valor == other.valor:
            if self.cod_tipo > other.cod_tipo:
                return True
            elif self.cod_tipo == other.cod_tipo:
                return self.descricao > other.descricao
        return False

    def __ge__(self, other):
        assert isinstance(other, Bem), "other nao e' do tipo Bem: {}".format(type(other))
        return self.valor >= other.valor

    def __get_cod_tipo(self):
        return self.__cod_tipo

    def __get_desc_tipo(self):
        return self.__desc_tipo

    def __get_descricao(self):
        return self.__descricao

    def __get_valor(self):
        return self.__valor

    def __set_cod_tipo(self, value):
        self.__cod_tipo = value

    def __set_desc_tipo(self, value):
        self.__desc_tipo = value

    def __set_descricao(self, value):
        self.__descricao = value

    def __set_valor(self, value):
        self.__valor = value

    cod_tipo = property(__get_cod_tipo, __set_cod_tipo)
    desc_tipo = property(__get_desc_tipo, __set_desc_tipo)
    descricao = property(__get_descricao, __set_descricao)
    valor = property(__get_valor, __set_valor)
