
def compararQuantidadeBens(v, obj1, obj2):
    if len(obj1.getListaBens()) > len(obj2.getListaBens()):
        return 1
    elif len(obj1.getListaBens()) > len(obj2.getListaBens()):
        return -1
    return 0
    
def compararQuantidadeBensDecre(v, obj1, obj2):
    return compararQuantidadeBens(v, obj1,obj2) *(-1)

def compararPartido(v, obj1,obj2):
    partido1 = obj1.getNomePartido()
    partido2 = obj2.getNomePartido()
    for x in range(len(partido1)):
        if x > len(obj2):
            return 1
        if partido1[x] > partido2[x]:
            return 1
        elif partido1[x] < partido2[x]:
            return -1
        elif partido1[x] == partido2[x]:
            return 0
def compararPartidoDecre(v, obj1,obj2): 
    return compararPartido(v, obj1,obj2)*(-1)

def compararNasc(v, obj1, obj2):
    data1 = obj1.getDataNascimento()
    data2 = obj2.getDataNascimento()
    data1 = data1[6:] + data1[3:5] +data1[:2]
    data2 = data2[6:] + data2[3:5] +data2[:2]
    if data1 > data2:
        return 1
    elif data1 < data2:
        return -1
    return 0

def compararNascDecre(v, obj1, obj2):
    return compararNasc(v, obj1, obj2)*(-1)