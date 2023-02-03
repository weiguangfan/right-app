import math


def UserSimilarity(train):
    W = dict()
    for u in train.keys():
       for v in train.keys():
           if u == v:
               continue
           # train[u],train[v]均为set()
           # W[u][v]为dict 嵌套，{“Ua”：{“Ub”：“分子”}
           # 两个用户各自对应的物品集，求交集
           # 分子，如果无交集会造成计算浪费；A,B两个用户，对应两对键值对，正常；
           W[u][v] = len(train[u] & train[v])
           # 分子除以分母
           W[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    return W