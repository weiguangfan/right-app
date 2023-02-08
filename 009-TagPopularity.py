def TagPopularity(records):
    tagfreq = dict()
    for user,item,tag in records:
        if tag not in tagfreq:
            tagfreq[tag] = 1
        else:
            tagfreq[tag] += 1
    return tagfreq



