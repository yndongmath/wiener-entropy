#-*- coding: gbk -*-
import codecs
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


def calcTree(num_ver):

 
    graph_path = ".\\graphs\\"

    test_name = 'trees'+ str(num_ver)
    graph_file_name = graph_path + test_name  +  '.g6'

    graphs = nx.read_graph6(graph_file_name)

    output_locate = ".\\"
    resultFile = output_locate + test_name +  '.csv'
    pff = codecs.open(resultFile, 'w', 'ascii')
    outPutStr = "graphNo, Vertex-Num, radius, diameter, entropy\n"
    pff.write(outPutStr)

    num = len(graphs)
    for count in range(num):
        print ("*****************==== srart computing RandicMeasures of graph  G%d ====************" % (count))
        G = graphs[count]
        connectFlag = nx.is_connected(G)
        if connectFlag != True:
            print("graph  % is not connected !"%(count))
            continue
        ###########################################
        ###########################################
        ###########################################
        ###########################################

        li2 = []
        li2.append(str(count))
        numVertex = nx.number_of_nodes(G)
        li2.append(str(numVertex))
        # radius,
        rad = nx.radius(G)
        temp = round(rad, 4)
        li2.append(str(temp))
        # diameter,
        dia = nx.diameter(G)
        temp = round(dia, 4)
        li2.append(str(temp))
        ###########################################
        ev = graphEntropy(G)
        ev = round(ev, 5)
        li2.append(str(ev))

        ############################################
        aaStr = ", "
        outPutStr = aaStr.join(li2) + "\n"

        pff.write(outPutStr)
        print("===== the values are %s" % (outPutStr))

        ################################################################################################################################

    pff.close()


if __name__ == '__main__':

    num_ver = 6
    while(num_ver < 19):
        calcTree(num_ver)
        num_ver = num_ver + 1

