import networkx as nx
import matplotlib.pyplot as pl

edgeData = []
with open('data/facebook-wall.txt.anon', 'r') as file:
    for line in file:
        words = line.split()
        if words[0] != words[1]:
            edgeData.append((words[0], words[1]))

g = nx.MultiDiGraph(edgeData)
degDist = nx.degree_histogram(g)
pl.ion()
pl.figure()
pl.xscale('log')
pl.yscale('log')
pl.scatter()
pl.show()
