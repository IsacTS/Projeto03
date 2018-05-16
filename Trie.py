# -*- coding: UTF-8 -*-
"""
Universidade Federal de Pernabuco -- UFPE (http://www.ufpe.br)
Centro de Informática -- CIn (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 -- Algoritmos e Estruturas de Dados

Autor:  Isac Tomaz da Silva
Email:  its@cin.ufpe.br
Data:   2018-05-16

Descrição:  Terceiro projeto de Algoritmos. Foi implementada a árvore Trie com
            objetivo de reduzir o tempo gasto na inserção dos bens dos
            candidatos.

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
        """Inicializa o no raiz e o tamanho.

        Cria um nó raiz e inicializa o tamanho da árvore como zero. Se for
        passado como parâmetro um dicionário inseri as chaves e os seus
        respectivos valores na árvore de prefixo."""
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
        if not no.end:
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
        """Recebi uma chave, se ela existir retorna seu valor."""
        return self.buscar(key)

    def __setitem__(self, key, value):
        """Cria ou troca um value de Trie.

        Substituí um valor da árvore de prefixo através da chave fornecida,
        se esse chave não exitir, cria essa chave fornecida para esse valor."""
        self.inserir(key, value)

    def __contains__(self, key):
        """Verifica se a chave está na árvore de prefixo pelo o in.

        Tenta procura a chave na árvore, se ela existir retorna True,
        caso contrário o __getitem__ dará KeyError porque a chave não
        existe resultando no retornado False."""
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False
