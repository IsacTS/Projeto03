# -*- coding: UTF-8 -*-
"""
Universidade Federal de Pernabuco -- UFPE (http://www.ufpe.br)
Centro de Informática -- CIn (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 -- Algoritmos e Estruturas de Dados

Autor:  Isac Tomaz da Silva
Email:  its@cin.ufpe.br

Descrição:  Terceiro projeto de Algoritmos.
Anexo:  https://github.com/IsacTS/Projeto03

Licença: The MIT License (MIT)
            Copyright(c) 2018 Isac Silva
"""


class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.filhos = [None] * 10
        self.end = False

    def __repr__(self):
        return self.value.__repr__()


class Trie(object):
    def __init__(self):
        self.raiz = Node()

    def inserir(self, key, item):
        no = self.raiz

        def index(caractere): return ord(caractere) - ord("0")
        for caractere in key:
            if no.filhos[index(caractere)] is None:
                no.filhos[index(caractere)] = Node()
            no = no.filhos[index(caractere)]
        no.value = item
        no.end = True

    def buscar(self, key):
        no = self.raiz

        def index(caractere): return ord(caractere) - ord("0")
        for caractere in key:
            if no.filhos is None:
                raise KeyError()
            no = no.filhos[index(caractere)]
        if not no.end:
            raise KeyError()
        return no.value
