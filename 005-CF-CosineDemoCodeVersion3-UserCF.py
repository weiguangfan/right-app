import math

# 根据论文公式，惩罚了用户u和用户v共同兴趣列表中热门物品对他们相似度的影响。
def UserSimilarity(train):
    # build inverse table for item_users
    item_users = dict()
    for u, items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # calculate co-rated items between users
    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] += 1/ math.log(1 + len(users))
    # calculate finial similarity matrix W
    W = dict()
    for u, related_users in C.items():
        for v,cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W