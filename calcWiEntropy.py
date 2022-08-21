import networkx as nx
import numpy as np
import math

import matplotlib.pyplot as plt
from networkx.generators.atlas import graph_atlas_g

np.set_printoptions(precision=4,suppress=True)


def DisMatrix(G):
    n = G.number_of_nodes()
    nodes = G.nodes()
    disList = []
    for k in nodes:
        dis = nx.single_source_shortest_path_length(G, k)
        disValue = list(dis.values())
        total = np.sum(np.array(disValue))
        disList.append(total)
    return disList

def entropy(c):
    length = len(c)
    if(length < 1):
        return -1

    result = 0

    for x in c:
        result = result - x * math.log(x,2)

    return result

def calcEntropy(a):
    n = len(a)
    a = np.array(a)
    total = np.sum(a)
    if(total < 1):
        return -1
    b = a/total

    value = entropy(b)
    return value


def graphEntropy(G):
    disList = DisMatrix(G)
    entropyValue = calcEntropy(disList)
    return entropyValue


if __name__ == '__main__':
    
    i = 1
    iEnd = 1253

    while i < iEnd:
        G = graph_atlas_g()[i]
        n = nx.number_of_nodes(G)
        m = nx.number_of_edges(G)

        connectFlag = nx.is_connected(G)
        if connectFlag != True:
            i = i + 1
            continue
        ###########################################
        treeFlag = 0
        biFlag = 0
        if (m < n):
            treeFlag = 1
            biFlag = 1
        else:
            flag = nx.is_bipartite(G)
            if(flag):
                biFlag = 1

        # print(biFlag)
        ###########################################
        # diameter,
        dia = nx.diameter(G)
        dia = round(dia, 4)
        ###########################################
        # print(i)
        en = graphEntropy(G)
        en = round(en, 5)
        aaa = [i, n, m, treeFlag, biFlag, en]
        print(aaa)
        i = i + 1
        ###########################################




