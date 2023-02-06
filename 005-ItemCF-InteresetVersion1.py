def Recommendation(train,user_id,W,K):
    rank = dict()
    ru = train[user_id]
    for i,pi in ru.items():
        for j,wj in sorted(
                W[i].items(),
                reverse=True
        )[0:K]:
            if j in ru:
                continue
            rank[j] += pi * wj
    return rank





