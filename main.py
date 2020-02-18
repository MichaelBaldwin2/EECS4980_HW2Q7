import networkx as nx
import matplotlib.pyplot as pl

g = nx.MultiDiGraph()
with open('data/facebook-wall.txt.anon', 'r') as file:
    for iLine in file:
        words = iLine.split()
        if len(words) >= 2 and words[0] != words[1]:
            g.add_edge(words[0], words[1])

degDist = nx.degree_histogram(g)
pl.ion()
pl.figure()
pl.bar(list(range(len(degDist))), degDist)
