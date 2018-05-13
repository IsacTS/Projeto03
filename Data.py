class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = int(dia)
        self.__mes = int(mes)
        self.__ano = int(ano)

    def __get_dia(self):
        return self.__dia

    def __get_mes(self):
        return self.__mes

    def __get_ano(self):
        return self.__ano

    def __set_dia(self, value):
        assert type(value) is int, "valor nao e' um inteiro: {}".format(value)
        self.__dia = value

    def __set_mes(self, value):
        assert type(value) is int, "valor nao e' um inteiro: {}".format(value)
        self.__mes = value

    def __set_ano(self, value):
        assert type(value) is int, "valor nao e' um inteiro: {}".format(value)
        self.__ano = value

    dia = property(__get_dia, __set_dia)
    mes = property(__get_mes, __set_mes)
    ano = property(__get_ano, __set_ano)

    @classmethod
    def to_data(cls, value):
        if isinstance(value, Data):
            return value
        dia, mes, ano = value.split('/')
        return Data(dia, mes, ano)

    def __str__(self):
        return '{0:0>2}/{1:0>2}/{2}'.format(self.__dia, self.__mes, self.__ano)
