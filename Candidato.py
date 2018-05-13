from Data import *
from Lista import Lista
from Trie import Trie
from Bem import Bem
from collections import defaultdict
import locale
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


class Candidato:

    def __init__(self, eleicao=None,
                 uf=None,
                 cod_cargo=None,
                 desc_cargo=None,
                 nome=None,
                 num_seq=None,
                 num_urna=None,
                 cpf=None,
                 nome_urna=None,
                 num_partido=None,
                 nome_partido=None,
                 sigla_partido=None,
                 cod_profissao=None,
                 profissao=None,
                 data_nasc=None,
                 sexo=None,
                 instrucao=None,
                 estado_civil=None,
                 uf_nasc=None,
                 nome_municipio=None,
                 sit_pleito=None,
                 sit_cand=None):
        '''
        Constructor
        '''
        self.__eleicao = int(eleicao)
        self.__uf = uf
        self.__cod_cargo = int(cod_cargo)
        self.__desc_cargo = desc_cargo
        self.__nome = nome
        self.__num_seq = num_seq
        self.__num_urna = num_urna
        self.__cpf = cpf
        self.__nome_urna = nome_urna
        self.__num_partido = int(num_partido)
        self.__nome_partido = nome_partido
        self.__sigla_partido = sigla_partido
        self.__cod_profissao = int(cod_profissao)
        self.__profissao = profissao
        self.__data_nasc = Data.to_data(data_nasc)
        self.__sexo = sexo
        self.__instrucao = instrucao
        self.__estado_civil = estado_civil
        self.__uf_nasc = uf_nasc
        self.__nome_municipio = nome_municipio
        self.__sit_pleito = sit_pleito
        self.__sit_cand = sit_cand
        self.__bens = Lista()

    def __str__(self):
        saida = '{} -- {} -- {}\n'.format(self.nome_urna, self.num_urna, self.sigla_partido)
        saida += '{} ({})\n'.format(self.desc_cargo, self.uf)
        saida += 'Resumo dos bens:\n'
        saida += 'Total declarado: R${}\n'.format(
            locale.currency(self.total_bens(), grouping=True, symbol=False))
        saida += '\n'.join(['{}: R${}'.format(chave, locale.currency(valor, grouping=True, symbol=False))
                            for chave, valor in self.total_bens_por_tipo().items()])
        return saida+'\n'

    def __repr__(self):
        return self.__str__()

    def inserirBem(self, bem):
        assert isinstance(bem, Bem), "bem nao e' um objeto da classe Bem: {}".format(type(bem))
        self.__bens.inserir(bem)

    def total_bens(self):
        soma = 0.0
        for bem in self.__bens:
            soma += bem.valor
        return soma

    def total_bens_por_tipo(self):
        resultado = defaultdict(float)
        for bem in self.__bens:
            resultado[bem.desc_tipo] += bem.valor
        return resultado

    def __eq__(self, other):
        if not isinstance(other, Candidato):
            return False
        return self.nome == other.nome and self.cpf == other.cpf

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        assert isinstance(other, Candidato), "other nao e' Candidato: {}".format(type(other))
        return self.nome < other.nome

    def __le__(self, other):
        assert isinstance(other, Candidato), "other nao e' Candidato: {}".format(type(other))
        return self.nome <= other.nome

    def __gt__(self, other):
        assert isinstance(other, Candidato), "other nao e' Candidato: {}".format(type(other))
        return self.nome > other.nome

    def __ge__(self, other):
        assert isinstance(other, Candidato), "other nao e' Candidato: {}".format(type(other))
        return self.nome >= other.nome

    def __get_nome_municipio(self):
        return self.__nome_municipio

    def __get_sit_pleito(self):
        return self.__sit_pleito

    def __get_sit_cand(self):
        return self.__sit_cand

    def __set_nome_municipio(self, value):
        self.__nome_municipio = value

    def __set_sit_pleito(self, value):
        self.__sit_pleito = value

    def __set_sit_cand(self, value):
        self.__sit_cand = value

    def __get_eleicao(self):
        return self.__eleicao

    def __get_uf(self):
        return self.__uf

    def __get_cod_cargo(self):
        return self.__cod_cargo

    def __get_desc_cargo(self):
        return self.__desc_cargo

    def __get_nome(self):
        return self.__nome

    def __get_num_seq(self):
        return self.__num_seq

    def __get_num_urna(self):
        return self.__num_urna

    def __get_cpf(self):
        return self.__cpf

    def __get_nome_urna(self):
        return self.__nome_urna

    def __get_num_partido(self):
        return self.__num_partido

    def __get_nome_partido(self):
        return self.__nome_partido

    def __get_sigla_partido(self):
        return self.__sigla_partido

    def __get_cod_profissao(self):
        return self.__cod_profissao

    def __get_profissao(self):
        return self.__profissao

    def __get_data_nasc(self):
        return self.__data_nasc

    def __get_sexo(self):
        return self.__sexo

    def __get_instrucao(self):
        return self.__instrucao

    def __get_estado_civil(self):
        return self.__estado_civil

    def __get_uf_nasc(self):
        return self.__uf_nasc

    def __set_eleicao(self, value):
        self.__eleicao = value

    def __set_uf(self, value):
        self.__uf = value

    def __set_cod_cargo(self, value):
        self.__cod_cargo = value

    def __set_desc_cargo(self, value):
        self.__desc_cargo = value

    def __set_nome(self, value):
        self.__nome = value

    def __set_num_seq(self, value):
        self.__num_seq = value

    def __set_num_urna(self, value):
        self.__num_urna = value

    def __set_cpf(self, value):
        self.__cpf = value

    def __set_nome_urna(self, value):
        self.__nome_urna = value

    def __set_num_partido(self, value):
        self.__num_partido = value

    def __set_nome_partido(self, value):
        self.__nome_partido = value

    def __set_sigla_partido(self, value):
        self.__sigla_partido = value

    def __set_cod_profissao(self, value):
        self.__cod_profissao = value

    def __set_profissao(self, value):
        self.__profissao = value

    def __set_data_nasc(self, value):
        assert isinstance(value, Data), "valor nao e' um objeto data: {}".format(value)
        self.__data_nasc = value

    def __set_sexo(self, value):
        self.__sexo = value

    def __set_instrucao(self, value):
        self.__instrucao = value

    def __set_estado_civil(self, value):
        self.__estado_civil = value

    def __set_uf_nasc(self, value):
        self.__uf_nasc = value

    eleicao = property(__get_eleicao, __set_eleicao)
    uf = property(__get_uf, __set_uf)
    cod_cargo = property(__get_cod_cargo, __set_cod_cargo)
    desc_cargo = property(__get_desc_cargo, __set_desc_cargo)
    nome = property(__get_nome, __set_nome)
    num_seq = property(__get_num_seq, __set_num_seq)
    num_urna = property(__get_num_urna, __set_num_urna)
    cpf = property(__get_cpf, __set_cpf)
    nome_urna = property(__get_nome_urna, __set_nome_urna)
    num_partido = property(__get_num_partido, __set_num_partido)
    nome_partido = property(__get_nome_partido, __set_nome_partido)
    sigla_partido = property(__get_sigla_partido, __set_sigla_partido)
    cod_profissao = property(__get_cod_profissao, __set_cod_profissao)
    profissao = property(__get_profissao, __set_profissao)
    data_nasc = property(__get_data_nasc, __set_data_nasc)
    sexo = property(__get_sexo, __set_sexo)
    instrucao = property(__get_instrucao, __set_instrucao)
    estado_civil = property(__get_estado_civil, __set_estado_civil)
    uf_nasc = property(__get_uf_nasc, __set_uf_nasc)
    nome_municipio = property(__get_nome_municipio, __set_nome_municipio)
    sit_pleito = property(__get_sit_pleito, __set_sit_pleito)
    sit_cand = property(__get_sit_cand, __set_sit_cand)
