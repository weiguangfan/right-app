import pandas as pd
import numpy as np
from pprint import pprint

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

# 计算所有的数据两两的杰卡德相似系数
from sklearn.metrics.pairwise import pairwise_distances
# 计算物品间相似度
item_similar = 1 - pairwise_distances(df.values.T, metric="jaccard")
item_similar = pd.DataFrame(item_similar, columns=items, index=items)
print("物品之间的两两相似度：")
print(item_similar)

topN_items = {}
# 遍历每一行数据
for i in item_similar.index:
    # 取出每一列数据，并删除自身，然后排序数据
    _df = item_similar.loc[i].drop([i])
    _df_sorted = _df.sort_values(ascending=False)

    top2 = list(_df_sorted.index[:2])
    topN_items[i] = top2

print("Top2相似物品：")
pprint(topN_items)

reco_res = {}
# 构建推荐结果
for user in df.index:    # 遍历所有用户
    res = set()
    # 获取用户已经购买的物品
    buyed_items = df.loc[user].replace(False,np.nan).dropna().index
    for item in buyed_items:
        # 根据每个物品找出最相似的TOP-N物品，构建初始推荐结果
        res = res.union(topN_items[item])
    # 过滤掉用户已购的物品
    res -= set(df.loc[user].replace(False,np.nan).dropna().index)
    # 添加到结果中
    reco_res[user] = res

print("最终推荐结果：")
pprint(reco_res)



