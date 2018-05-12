# -*- coding: UTF-8 -*-
"""
Universidade Federal de Pernabuco -- UFPE (http://www.ufpe.br)
Centro de Informática -- CIn (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 -- Algoritmos e Estruturas de Dados

Autor:  Isac Tomaz da Silva
Email:  its@cin.ufpe.br
Data:   2018-05-16

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
    def __init__(self, dic=None):
        self.raiz = Node()
        self.tamanho = 0
        if dic is not None and type(dic) is dict:
            for key, value in dic.items():
                self.inserir(key, value)

    def inserir(self, key, item):
        """Adiciona um valor na árvore de prefixo."""
        no = self.raiz

        def index(caractere): return ord(caractere) - ord("0")
        for caractere in key:
            if no.filhos[index(caractere)] is None:
                no.filhos[index(caractere)] = Node()
            no = no.filhos[index(caractere)]
        self.tamanho += 1
        no.value = item
        no.end = True

    def buscar(self, key):
        """Procura um valor na árvore de prefixo, pela sua chave."""
        no = self.raiz

        def index(caractere): return ord(caractere) - ord("0")
        for caractere in key:
            if no.filhos is None:
                raise KeyError()
            no = no.filhos[index(caractere)]
            if no is None:
                raise KeyError()
        if not no.end:
            raise KeyError()
        return no.value

    def __len__(self):
        """Retorna o tamanho da árvore de prefixo."""
        return self.tamanho

    def __getitem__(self, key):
        """Recebi uma chave e verifica se ela existe."""
        return self.buscar(key)

    def __setitem__(self, key, value):
        """Troca um value de Trie.

        Substituí um valor da árvore de prefixo através da chave fornecida.
        O self.tamanho -= 1, é porque não função inserir adiciona mais 1 no
        tamanho, para o tamanho continuar o mesmo já que só está sendo feito
        apenas um alteração de valor."""
        self.tamanho -= 1
        self.inserir(key, value)
