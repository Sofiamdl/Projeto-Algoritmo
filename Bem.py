class Bem:
    def __init__(self, dados):
        self.__codigoBem = dados[13]
        self.__descricaoBem = dados[14]
        self.__descricaoDetalhadaBem = dados[15]
        self.__valorBem = self.transformarFloat(dados[16])
    
    def __str__(self):
        return self.__codigoBem + ' -- ' + self.__descricaoBem + ' -- R$ ' + str(self.__valorBem) + ' -- Descrição: '+ self.__descricaoDetalhadaBem
   
    def __repr__(self):
        return self.__codigoBem + ' -- ' + self.__descricaoBem + ' -- R$ ' + str(self.__valorBem) + ' -- Descrição: '+ self.__descricaoDetalhadaBem
   
    def transformarFloat(self, num):
        numero = ''
        for x in num:
            if x != ',':
                numero += x
            else:
                numero+='.'
        return float(numero)

    def __eq__(self, bem):
        if self.__valorBem == bem.getValorBem():
            if self.__codigoBem == bem.getCodigoBem():
                if self.__descricaoDetalhadaBem == bem.getDescricaoDetalhadaBem():
                    return True
        return False

    def __ne__(self, bem):
        if not self == bem:
            return True
        return False

    def __lt__(self, bem):
        if self.__valorBem < bem.getValorBem():
            return True
        if self.__codigoBem < bem.getCodigoBem() and self.__valorBem == bem.getValorBem():
            return True
        if self.__descricaoDetalhadaBem < bem.getDescricaoDetalhadaBem() and self.__codigoBem == bem.getCodigoBem():
            return True
        return False

    def __le__(self, bem):
        if self < bem or self == bem:
            return True
        return False

    def __gt__(self, bem):
        if not self <= bem:
            return True
        return False

    def __ge__(self, bem):
        if self > bem or self == bem:
            return True
        return False
    

    def getCodigoBem(self):
        return self.__codigoBem
    def setCodigoBem(self, new):
        self.__codigoBem = new
    def getDescricaoBem(self):
        return self.__descricaoBem
    def setDescricaoBem(self, new):
        self.__descricaoBem = new
    def getDescricaoDetalhadaBem(self):
        return self.__descricaoDetalhadaBem
    def setDescricaoDetalhadaBem(self, new):
        self.__descricaoDetalhadaBem
    def getValorBem(self):
        return self.__valorBem
    def setValorBem(self, new):
        self.__valorBem = new
    





