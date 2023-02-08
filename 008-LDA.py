from scipy import rand
converged = True
# D为文档集合,D[i]是第i篇文档
D = ["DocId1","DocId2",]

# w[i][j]是第i篇文档中的第j个词
w = {"DocId1":["word1","word2"],}

K = 12
# z[i][j]是第i篇文档中第j个词属于的话题,假设一共有K个话题
Z = [{"DocId1":{"word1":"topic2","word2":"topic1"}},{"DocId2":{"word1":"topic3","word2":"topic4"}}]

# NZD(z,d)记录文档d中被赋予话题z的词的个数
NZD = {"DocId1":{"topic1":"word_count1","topic2":"word_count2"}}

# NWZ(w,z)记录词w被赋予话题z的次数
NWZ = {"word1":"topic_count1","word2":"topic_count2"}


def SampleTopic():
    for i in range(0,len(D)):
        for j in range(0,len(D[i])):
            Z[i][j] = rand() % K  # 给词随机分配话题
            # NZD[Z[i][j],D[i]] ++
            # NWZ[w[i][j],Z[i][j]] ++
            # NZ[Z[i][j]] ++
            pass


while not converged:
    for i in range(0,len(D)):
        for j in range(0,len(D[i])):
            pass
            # NWZ[w[i][j],z[i][j]] --
            # NZ[Z[i][j]] --
            # NZD[Z[i][j],D[i]] --
            # Z[i][j] = SampleTopic()
            # NWZ[w[i][j],Z[i][j]] ++
            # NZ[Z[i][j]] ++
            # NZD[Z[i][j],D[i]] ++