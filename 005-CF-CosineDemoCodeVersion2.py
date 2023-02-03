import math

# 想去筛选，两个用户各自对应的物品集的交集，不为空的用户，再去计算；
def UserSimilarity(train):
    # build inverse table for item_users
    # 得到每个物品对应的用户集合
    item_users = dict()  # {“Ia”：{“Ua”，“Ub”}}
    for u,items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()  # 不重复的集合；
            item_users[i].add(u)

    # calculate co-rated items between users
    # 找出有交集物品的用户对
    C = dict()  # 不同用户共同关注的物品数 {"Ua":{"Ub":3},"Ub":{"Ua":3}}
    N = dict()  # 用户关注的物品数  {"Ua":"1"}
    for i, users in item_users.items():
        for u in users:
            N[u] += 1  # 物品遍历完，值会一直增加，数字代表用户关注的物品数
            for v in users:
                if u == v:
                    continue
                # 产生很多用户对，并且是关注过同一个物品的；
                # 物品遍历完，值会一直增加，数字代表用户对共同关注的物品数
                # A,B两个用户，对应两对键值对，正常；
                C[u][v] += 1

    # calculate finial similarity matrix W
    W = dict()  # {"Ua":{"Ub":0.73}
    for u,related_users in C.items():
        for v,cuv in related_users.items():
            # cuv 代表两个用户关注的物品集的交集
            # N[u],N[v] 代表用户各自关注的物品集的数量
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W