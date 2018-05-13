from operator import attrgetter


class _No:

    def __init__(self, item=None, ante=None, prox=None):
        self.item = item
        self.prox = prox
        self.ante = ante


class Lista:

    def __init__(self):
        self.__primeiro = self.__ultimo = _No()

    def vazia(self):
        return self.__primeiro == self.__ultimo

    def pesquisa(self, item, key=None):
        chave = key is not None and attrgetter(key) or (lambda x: x)
        aux = self.__primeiro.prox
        while not aux is None and chave(aux.item) != item:
            aux = aux.prox
        if aux is None:
            raise ValueError
        return aux.item

    def inserir(self, item):
        self.__ultimo.prox = _No(item, self.__ultimo, None)
        self.__ultimo = self.__ultimo.prox

    def inserirInicio(self, item):
        aux = _No(item, self.__primeiro, self.__primeiro.prox)
        self.__primeiro.prox = aux
        if self.vazia():
            self.__ultimo = aux
        else:
            aux.prox.ante = aux

    def inserirOrdenado(self, item, cmp=lambda o1, o2: o1 <= o2):
        if self.vazia():
            self.inserir(item)
            return
        ref = self.__primeiro
        while not ref.prox is None and cmp(ref.prox.item, item):
            ref = ref.prox
        aux = _No(item, ref, ref.prox)
        ref.prox = aux
        if aux.prox is None:
            self.__ultimo = aux
        else:
            aux.prox.ante = aux

    def removerInicio(self):
        if(self.vazia()):
            return None
        aux = self.__primeiro.prox
        self.__primeiro.prox = aux.prox
        item = aux.item
        if self.__ultimo == aux:
            self.__ultimo = self.__primeiro
        else:
            aux.prox.ante = self.__primeiro
        aux.prox = None
        del aux
        return item

    def removerFim(self):
        if(self.vazia()):
            return None
        aux = self.__ultimo
        self.__ultimo = aux.ante
        self.__ultimo.prox = None
        item = aux.item
        aux.prox = aux.ante = None
        del aux
        return item

    def __str__(self):
        aux = self.__primeiro.prox
        s = "["
        while not aux is None:
            s += str(aux.item) + ','
            aux = aux.prox

        s = s.strip(',')
        s += "]"
        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.__atual = self.__primeiro.prox
        return self

    def __next__(self):
        if self.__atual is None:
            raise StopIteration
        item = self.__atual.item
        self.__atual = self.__atual.prox
        return item
