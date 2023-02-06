import random


class NegativeSample():

    def RandomSelectNegatieSample(self,items,items_pool):
        """

        :param items: items是一个dict，它维护了用户已经有过行为的物品的集合。
        :param items_pool: items_pool维护了候选物品的列表，在这个列表中，物品i出现的次数和物品i的流行度成正比。
        :return:按照物品的流行度采样出了那些热门的、但用户却没有过行为的物品
        """
        ret = dict()
        for i in items.keys():
            ret[i] = 1
        n = 0
        for i in range(0,len(items)*3):
            item = items_pool[random.randint(0,len(items_pool) - 1)]
            if item in ret:
                continue
            ret[item] = 0
            n += 1
            if n > len(items):
                break
        return ret