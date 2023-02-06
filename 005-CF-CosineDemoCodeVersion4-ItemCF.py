import math


def ItemSimilarity(train):
    # calculate co-rated users between items
    C = dict()
    N = dict()
    for u,items in train.items():
        for i in items:
            N[i] += 1
            for j in items:
                if i == j:
                    continue
                C[i][j] += 1
    # calculate finial similarity matrix W
    W = dict()
    for i,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W





