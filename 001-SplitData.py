import random

def SplitDate(data,M,K,seed):
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0,M) == K:
            test.append([user,item])
        else:
            train.append([user,item])
    return train,test