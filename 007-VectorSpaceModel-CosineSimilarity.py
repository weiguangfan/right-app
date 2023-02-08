import math


def addToVec():
    pass


def CosineSimilarity(entity_items):
    w = dict()
    ni = dict()
    for e,items in entity_items.items():
        for i,wie in items.items():
            addToVec(ni,i,wie*wie)
            for j,wje in items.items():
                addToVec(w,i,j,wie,wje)
    for i,relate_items in w.items():
        relate_items = {x:y/math.sqrt(ni[i] * ni[x]) for x,y in relate_items.items()}
    pass


def CalculateSimilarity(D):
    w = dict()
    for di in D:
        for dj in D:
            w[di][dj] = CosineSimilarity(di,dj)
    return w