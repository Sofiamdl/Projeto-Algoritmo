from Lista import *
class Candidato:
    def __init__(self, dados):
        dadosL = dados[1:len(dados)-2].split('";"')
        self.__anoEleicao = dadosL[2]
        self.__siglaUF = dadosL[10]
        self.__codigoCargo = dadosL[13]
        self.__descricaoCargo = dadosL[14]
        self.__nomeCandidato = dadosL[17]
        self.__IDCandidato = dadosL[15] 
        self.__numeroUrna = dadosL[16]
        self.__CPF = dadosL[20]
        self.__nomeUrna = dadosL[18]
        self.__numeroPartido = dadosL[27]
        self.__nomePartido = dadosL[29]
        self.__siglaPartido = dadosL[28]
        self.__codigoOcupacao = dadosL[49]
        self.__descricaoOcupacao = dadosL[50]
        self.__dataNascimento = dadosL[38]
        self.__sexoCandidato = dadosL[42]
        self.__grauInstrucao = dadosL[44]
        self.__estadoCivil = dadosL[46]
        self.__UFnascimento = dadosL[35]
        self.__municipioNascimento = dadosL[37]
        self.__situacaoPosPleito = dadosL[53]
        self.__situacaoCandidatura = dadosL[25]
        self.__listaBens = ListaDuplamenteEncadeada()

    def __str__(self):
        return self.__nomeUrna + " -- " + self.__numeroUrna + ' -- ' + self.__siglaPartido +'\n'+ self.__descricaoCargo+' '+ self.__siglaUF+' ' + self.__municipioNascimento +' '+ self.__UFnascimento+ '\n    -Total declarado: R$'+ str(float(self.valorTotal()))+ '\n    -Total por tipo de bem: '+ self.valoresBem()

    def __repr__(self):
        return self.__nomeUrna + " -- " + self.__numeroUrna + ' -- ' + self.__siglaPartido +'\n'+ self.__descricaoCargo+' '+ self.__siglaUF+' ' + self.__municipioNascimento +' '+ self.__UFnascimento+ '\n    -Total declarado: R$'+ str(float(self.valorTotal()))+ '\n    -Total por tipo de bem: '+ self.valoresBem()


    def valorTotal(self):
        valor = 0
        for x in self.__listaBens:
            valor += x.getValorBem()
        return valor

    def valoresBem(self):
        string = ''
        for x in self.__listaBens:
            string +='\n           ' + x.getDescricaoBem() + ': R$' + str(x.getValorBem())
        return string

    def incluirBem(self, bem):
        self.__listaBens.anexar(bem)
    
    def exibirBens(self):
        for bens in self.__listaBens:
            print(bens)

    def __eq__(self, candidato):
        if self.__nomeCandidato == candidato.getNomeCandidato():
            if self.__CPF == candidato.getCPF():
                return True
        return False

    def __ne__(self, candidato):
        if not self == candidato:
            return True
        return False

    def __lt__(self, candidato):
        nomeCand = candidato.getNomeUrna()
        if self.__nomeUrna == nomeCand:
            if self.__CPF == candidato.getCPF():
                return False
            else:
                x = min(self.__CPF, candidato.getCPF())
                if x == self.__CPF:
                    return True
                else:
                    return False
        x = min(self.__nomeUrna, nomeCand)
        if x == self.__nomeUrna:
            return True
        else:
            return False


    def __le__(self, candidato):
        if self < candidato or self == candidato:
            return True
        return False

    def __gt__(self, candidato):
        if not self < candidato:
            return True
        return False

    def __ge__(self, candidato):
        if self > candidato or self == candidato:
            return True
        return False

    def getAnoEleicao(self):
        return self.__anoEleicao 
    def setAnoEleicao(self, new):
        self.__anoEleicao = new
    def getSiglaUF(self):
        return self.__siglaUF
    def setSiglaUF(self, new):
        self.__siglaUF = new
    def getCodigoCargo(self):
        return self.__codigoCargo 
    def setCodigoCargo(self, new):
        self.__codigoCargo  = new
    def getDescricaoCargo(self):
        return self.__descricaoCargo
    def setDescricaoCargo(self,new):
        self.__descricaoCargo = new
    def getNomeCandidato(self):
        return self.__nomeCandidato
    def setNomeCandidato(self, new):
        self.__nomeCandidato = new
    def getIDCandidato(self):
        return self.__IDCandidato
    def setIDCandidato(self, new):
        self.__IDCandidato = new #(número sequencial do candidato gerado pelos sistemas eleitorais)
    def getNumeroUrna(self):
        return self.__numeroUrna
    def setNumeroUrna(self,new):
        self.__numeroUrna = new
    def getCPF(self):
        return self.__CPF
    def setCPF(self, new):
        self.__CPF = new
    def getNomeUrna(self):
        return self.__nomeUrna
    def setNomeUrna(self, new):
        self.__nomeUrna = new
    def getNumeroPartido(self):
        return self.__numeroPartido
    def setNumeroPartido(self, new):
        self.__numeroPartido = new
    def getNomePartido(self):
        return self.__nomePartido
    def setNomePartido(self, new):
        self.__nomePartido = new
    def getSiglaPartido(self):
        return self.__siglaPartido
    def setSiglaPartido(self, new):
        self.__siglaPartido = new
    def getCodigoOcupacao(self):
        return self.__codigoOcupacao
    def setCodigoOcupacao(self, new):
        self.__codigoOcupacao = new
    def getDescricaoOcupacao(self):
        return self.__descricaoOcupacao
    def setDescricaoOcupacao(self, new):
        self.__descricaoOcupacao = new
    def getDataNascimento(self):
        return self.__dataNascimento
    def setDataNascimento(self, new):
        self.__dataNascimento = new#(armazenada como dia, mês e ano)
    def getSexoCandidato(self):
        return self.__sexoCandidato
    def setSexoCandidato(self,new):
        self.__sexoCandidato = new
    def getGrauInstrucao(self):
        return self.__grauInstrucao
    def setGrauInstrucao(self, new):
        self.__grauInstrucao = new
    def getEstadoCivil(self):
        return self.__estadoCivil
    def setEstadoCivil(self, new):
        self.__estadoCivil = new
    def getUFnascimento(self):
        return self.__UFnascimento
    def setUFnascimento(self, new):
        self.__UFnascimento = new
    def getMunicipioNascimento(self):
        return self.__municipioNascimento
    def setMunicipioNascimento(self, new):
        self.__municipioNascimento = new
    def getSituacaoPosPleito(self):
        return self.__situacaoPosPleito
    def setSituacaoPosPleito(self, new):
        self.__situacaoPosPleito = new#(eleito, não eleito, suplente)
    def getSituacaoCandidatura(self):
        return self.__situacaoCandidatura
    def setSituacaoCandidatura(self,new):
        self.__situacaoCandidatura = new#(deferida ou indeferida)
    def getListaBens(self):
        return self.__listaBens
   


