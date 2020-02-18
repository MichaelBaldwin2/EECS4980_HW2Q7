import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

edgeData = []
with open('data/facebook-wall.txt.anon', 'r') as file:
    for line in file:
        words = line.split()
        if words[0] != words[1]:
            edgeData.append((words[1], words[0]))
G = nx.DiGraph(edgeData)

# inDegree = list(g.in_degree())
# outDegree = list(g.out_degree())
# degDist = nx.degree_histogram(g)
plt.ion()
plt.figure()
# plt.xscale('log')
# plt.yscale('log')
# plt.scatter(inDegree, outDegree)
# plt.show()

def plot_degree_dist(G):
    inDegrees = [G.in_degree(n) for n in G.nodes()]
    outDegrees = [G.out_degree(n) for n in G.nodes()]
    degDist = nx.degree_histogram(G)
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(range(len(degDist)), degDist, 'b')
    # plt.scatter(inDegrees, outDegrees)
    # plt.hist(inDegrees, bins=1)
    plt.show()

plot_degree_dist(G)



# degrees = G.in_degree()
# degree_counts = Counter(degrees)
# x, y = zip(*degree_counts.items())
#
# plt.figure()
#
# # prep axes
# plt.xlabel('degree')
# plt.xscale('log')
# # plt.xlim(1, max(x))
#
# plt.ylabel('frequency')
# plt.yscale('log')
# # plt.ylim(1, max(y))
#                                                                                                                                      # do plot
# plt.scatter(x, y, marker='.')
# plt.show()
