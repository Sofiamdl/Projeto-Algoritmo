from Candidato import *
from Bem import *
from Lista import *
from comparacoes import *
class Controle:
    def __init__(self):
        self.__listaCandidatos = ListaDuplamenteEncadeada()
        pass

    def listaCandidatos(self, arquivo):
        dados = open(arquivo, 'r')
        for x in dados:
            c = Candidato(x)
            if c.getCPF() != 'NR_CPF_CANDIDATO':
                self.__listaCandidatos.inserir_ordenado(c)
        
    def adicionarBens(self, arquivo):
        dados = open(arquivo, 'r')
        dicionarioBens ={}
        for x in dados:
            bem = x[1:len(x)-2].split('";"')
            if bem[11] not in dicionarioBens:
                dicionarioBens[bem[11]] = []
            dicionarioBens[bem[11]].append(bem)
        for candidato in self.__listaCandidatos:
            if candidato.getIDCandidato() in dicionarioBens:
                for x in dicionarioBens[candidato.getIDCandidato()]:
                    bem = Bem(x)
                    candidato.incluirBem(bem)
        del dicionarioBens
        del dados

    def listaPartido(self, partido):
        listaPartido = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.getNomePartido()== partido or x.getSiglaPartido() == partido:
                listaPartido.anexar(x)
        return listaPartido

    def listaUF(self, UF):
        listaUF = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.getSiglaUF()== UF:
                listaUF.anexar(x)
        return listaUF
        
    def listaNascidosMunicipio(self, municipio):
        listaNascidosMunicipio = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.getUFNascimento() == municipio:
                listaNascidosMunicipio.anexar(x)
        return listaNascidosMunicipio
        
    def listaCargo(self, cargo):
        listaCargo = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.getDescricaoCargo()== cargo or x.getCodigoCargo()== cargo:
                listaCargo.anexar(x)
        return listaCargo
        
    def listaBensAcimaValor(self, valor):
        listaBensAcimaValor = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.valorTotal() >= valor :
                listaBensAcimaValor.anexar(x)
        return listaBensAcimaValor

    def listaPleito(self,pleito):
        listaPleito = ListaDuplamenteEncadeada()
        for x in self.__listaCandidatos:
            if x.getSituacaoPosPleito() == pleito:
                listaPleito.anexar(x)
        return listaPleito

    def printarListaCriterio(self, criterio, tipo):
        if tipo == 'partido':
            print(self.listaPartido(criterio))
        elif tipo == 'UF':
            print(self.listaUF(criterio))
        elif tipo == 'nascidos':
            print(self.listaNascidosMunicipio(criterio))
        elif tipo == 'cargo':
            print(self.listaCargo(criterio))
        elif tipo == 'bens':
            print(self.listaBensAcimaValor(criterio))
        elif tipo == 'pleito':
            print(self.listaPleito(criterio))
            
    def mediaTotalUF(self, UF):
        var = 0
        cont = 0
        for x in self.__listaCandidatos:
            if x.getSiglaUF()== UF:
                var += len(x.getListaBens)
                cont += 1
        return var / cont

    def mediaTotalCargo(self, cargo):
        var = 0
        cont = 0
        for x in self.__listaCandidatos:
            if x.getDescricaoCargo()== cargo or x.getCodigoCargo()== cargo:
                var += len(x.getListaBens())
                cont += 1
        return var / cont

    def mediaTotalPartido(self, partido):
        var = 0
        cont = 0
        for x in self.__listaCandidatos:
            if x.getNomePartido()== partido or x.getSiglaPartido() == partido:
                var += len(x.getListaBens())
                cont += 1
        return var / cont

    def mediaTotalNascimento(self, municipio):
        var = 0
        cont = 0
        for x in self.__listaCandidatos:
            if x.getUFNascimento() == municipio:
                var += len(x.getListaBens())
                cont += 1
        return var / cont

    def mediaTotalOcupacao(self, ocupacao):
        var = 0
        cont = 0
        for x in self.__listaCandidatos:
            if x.getCodigoOcupacao() == ocupacao or x.getDescricaoOcupacao == ocupacao:
                var += len(x.getListaBens())
                cont += 1
        return var / cont

    def removerCriterio(self, criterio, tipo):
        ind = 0
        if tipo == 'UF':
            for x in self.__listaCandidatos:
                if x.getSiglaUF()== criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind+=1
        elif tipo == 'cargo':
            for x in self.__listaCandidatos:
                if x.getDescricaoCargo()== criterio or x.getCodigoCargo()== criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind+=1
        elif tipo == 'partido':
            for x in self.__listaCandidatos:
                if x.getNomePartido()== criterio or x.getSiglaPartido() == criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind += 1
        elif tipo == 'nascimento':
            for x in self.__listaCandidatos:
                if x.getUFNascimento()== criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind += 1
        elif tipo == 'ocupacao':
            for x in self.__listaCandidatos:
                if x.getCodigoOcupacao() == criterio or x.getDescricaoOcupacao == criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind += 1
        elif tipo == 'eleito':
            for x in self.__listaCandidatos:
                if x.getSituacaoPosPleito() == criterio:
                    self.__listaCandidatos.selecionar(ind)
                else:
                    ind += 1

    def getListaCand(self):
        return self.__listaCandidatos
