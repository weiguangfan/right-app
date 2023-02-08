def CosineSim(item_tags,i,j):
    ret = 0
    for b,wib in item_tags[i].items():
        if b in item_tags[j]:
            ret += wib * item_tags[j][b]
