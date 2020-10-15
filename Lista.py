class ListaDuplamenteEncadeada:
    def __init__(self, objeto = None):
        self.ultimo = self.primeiro = No()
        self.lenLista = 0
        if objeto != None:
            for x in objeto:
                self.anexar(x)
            

    def __len__(self):
        return self.lenLista

    def __str__(self):
        string = ''
        if self.vazio():
            return string
        aux = self.primeiro
        while aux != self.ultimo.anterior:
            string += str(aux.prox.item) +'\n'
            aux = aux.prox
        string += str(aux.prox.item)
        return string

    def __repr__(self):
        return 'ListaDuplamenteEncadeada([' + self.__str__() + '])'
        
        
    def vazio(self):
        if self.ultimo == self.primeiro:
            return True

    def buscar(self, ind):
        if ind >= 0 and ind < self.lenLista:
            if ind > self.lenLista // 2:
                aux = self.primeiro
                while ind >= 0:
                    aux = aux.prox
                    ind -= 1
            else:
                aux = self.ultimo
                while ind < self.lenLista-1:
                    aux = aux.anterior
                    ind += 1
            if aux != self.primeiro:
                    return aux
        elif ind < 0 and ind >= (self.lenLista)*(-1):
            aux = self.ultimo
            while ind < -1:
                aux = aux.anterior
                ind += 1
            return aux
        raise IndexError

    def __getitem__(self, ind):
        return (self.buscar(ind)).item


    def __setitem__(self, ind, elem):
        aux = self.buscar(ind)
        aux.item = elem

    def indice(self, valor):
        aux = self.primeiro
        ind = 0
        for x in range(self.lenLista):
            if aux.prox.item == valor:
                return ind
            aux = aux.prox
            ind += 1
        raise ValueError

    def anexar(self, valor):
        self.ultimo.prox = No(valor, None, self.ultimo)
        self.ultimo = self.ultimo.prox
        self.lenLista += 1

    def selecionar(self, ind = None):
        if ind == None:
            ind = self.lenLista - 1
        aux = self.buscar(ind)
        aux.anterior.prox = aux.prox
        if aux != self.ultimo:
            aux.prox.anterior = aux.anterior
        else:
            self.ultimo = aux.anterior
        self.lenLista -= 1
        return aux.item   

    def inserir(self, ind, valor):
        if (self.vazio() and ind == 0) or ind == self.lenLista or ind == (-1):
            self.anexar(valor)
        else:
            aux = (self.buscar(ind)).anterior
            aux.prox.anterior = No(valor, aux.prox, aux)
            aux.prox = aux.prox.anterior
            self.lenLista += 1

    def inserir_ordenado(self, valor):
        if not self.vazio():
            if valor.getNomeUrna()[0] <= "M":
                aux = self.primeiro.prox
                while aux != None:
                    if self.comparar(valor, aux.item) == -1:
                        aux.anterior = No(valor,aux, aux.anterior)
                        aux.anterior.anterior.prox = aux.anterior
                        self.lenLista += 1
                        return
                    aux = aux.prox
            else:
                aux = self.ultimo
                while aux != self.primeiro:
                    if self.comparar(aux.item, valor) == -1:
                        if aux == self.ultimo:
                            self.ultimo.prox = No(valor,None,self.ultimo)
                            self.ultimo = self.ultimo.prox
                        else:
                            aux.prox = No(valor, aux.prox, aux)
                            aux.prox.prox.anterior = aux.prox
                        self.lenLista += 1
                        return
                    aux = aux.anterior
        self.ultimo.prox = No(valor,None,self.ultimo)
        self.ultimo = self.ultimo.prox
        self.lenLista += 1

    def concatenar(self, lista):
        if lista.primeiro != lista.ultimo:
            self.ultimo.prox = lista.primeiro.prox
            self.ultimo = lista.ultimo
            lista.primeiro = lista.ultimo = None
        return

    def __iter__(self):
        return Ponteiro(self)
    
    def comparar(self, obj1, obj2):
        if obj1 < obj2:
            return -1
        elif obj2 < obj1:
            return 1
        else:
            return 0


        
class No:
    def __init__(self, item = None, prox= None, anterior=None):
        self.item = item
        self.prox = prox
        self.anterior = anterior

    
class Ponteiro:
    def __init__(self, lista):
        self.posicao = lista.primeiro.prox

    def __next__(self):
        if self.posicao != None:
            valorDoNo = self.posicao.item
            self.posicao = self.posicao.prox
            return valorDoNo
        raise StopIteration

    def __iter__(self):
        return self
