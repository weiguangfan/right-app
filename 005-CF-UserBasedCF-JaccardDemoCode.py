from pprint import pprint

import pandas as pd
import numpy as np
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import pairwise_distances

users = ["User1", "User2", "User3", "User4", "User5"]
items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
# 用户购买记录数据集
datasets = [
    [1,0,1,1,0],
    [1,0,0,1,1],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,1,1,0,1],
]

df = pd.DataFrame(datasets,
                  columns=items,
                  index=users, dtype=np.bool)
print(df)
print(df.loc["User1"])

# 直接计算某两项的杰卡德相似系数
# 计算Item A 和Item B的相似度
# print(df["Item A"])
print(jaccard_score(df["Item A"], df["Item B"]))

# 计算所有的数据两两的杰卡德相似系数
# 计算用户间相似度
user_similar = 1 - pairwise_distances(df.values, metric="jaccard")
user_similar = pd.DataFrame(user_similar, columns=users, index=users)
print("用户之间的两两相似度：")
print(user_similar)
print(user_similar.index)
print(user_similar.loc['User1'])

# 计算物品间相似度
# item_similar = 1 - pairwise_distances(df.values.T, metric="jaccard")
# item_similar = pd.DataFrame(item_similar, columns=items, index=items)
# print("物品之间的两两相似度：")
# print(item_similar)

topN_users = {}
# 遍历每一行数据
for i in user_similar.index:
    # 取出每一列数据，并删除自身，然后排序数据
    _df = user_similar.loc[i].drop([i])
    # sort_values 排序 按照相似度降序排列
    _df_sorted = _df.sort_values(ascending=False)
    # 从排序之后的结果中切片 取出前两条（相似度最高的两个）
    top2 = list(_df_sorted.index[:2])
    topN_users[i] = top2

print("Top2相似用户：")
pprint(topN_users)

# 准备空dict用来保存推荐结果
reco_res = {}
# 遍历所有的最相似用户
for user, sim_users in topN_users.items():
    res = set()    # 存储推荐结果
    for sim_user in sim_users:
        # 构建初始的推荐结果
        res = res.union(set(df.loc[sim_user].replace(False,np.nan).dropna().index))
    # 过滤掉已经购买过的物品
    res -= set(df.loc[user].replace(False,np.nan).dropna().index)
    reco_res[user] = res
print("最终推荐结果：")
pprint(reco_res)
