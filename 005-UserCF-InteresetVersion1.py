def Recommend(user,train,W,K):
    rank = dict()  # {"Ia":0.44}

    # train[user] 用户user关注的物品集
    interacted_items = train[user]

    # W[user] {"Ua":{"Ub":0.36}}
    # 遍历 和用户u相似度靠前的K个用户；
    # v 相似用户
    # wuv 用户u和用户v的相似度
    for v,wuv in sorted(W[user].items,reverse=True)[0:K]:

        # train[v] 用户v关注的物品集
        # train {“Ua”：{“Ia”:0.36,"Ib":0.21}}
        # i 物品
        # rvi 用户v对物品i的兴趣
        # 遍历用户v关注的物品集
        for i,rvi in train[v].items:
            if i in interacted_items:
                # we should filter items user interacted before
                continue
            # 按照公式计算
            rank[i] += wuv * rvi
    return rank





