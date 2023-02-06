class InitModel():
    def __init__(self,v1,v2):
        pass


def RandSelectNegativeSamples():
    pass


def Predict():
    pass


def LatenFactorModel(user_items,F,N,alpha,lambda1):
    [P,Q] = InitModel(user_items,F)
    for step in range(0,N):
        for user, items in user_items.items():
            samples = RandSelectNegativeSamples(items)
            for item,rui in samples.items():
                eui = rui - Predict(user,item)
                for f in range(0,F):
                    P[user][f] += alpha*(eui * Q[item][f] - lambda1 * P[user][f])
                    Q[item][f] += alpha*(eui * P[user][f] - lambda1 * Q[item][f])
        alpha *= 0.9

def Recommend(user,P,Q):
    rank = dict()
    for f,puf in P[user].items():
        for i,qfi in Q[f].items():
            if i not in rank:
                rank[i] += puf * qfi
    return rank