import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

edgeData = []
with open('data/facebook-wall.txt.anon', 'r') as file:
    for line in file:
        words = line.split()
        if words[0] != words[1]:
            edgeData.append((words[1], words[0]))

g = nx.DiGraph(edgeData)
degDist = nx.degree_histogram(g)
npDD = np.asarray(degDist)

# Hist
plt.plot(range(len(npDD)), npDD, 'bo')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Freq')
plt.xlabel('Degree')
plt.show()
plt.clf()

# CCDF
s = float(npDD.sum())
cdf = npDD.cumsum(0) / s
ccdf = 1 - cdf
plt.plot(range(len(ccdf)), ccdf, 'b')
plt.xscale('log')
plt.yscale('log')
# plt.ylim([0, 1])
plt.ylabel('CCDF')
plt.xlabel('Degree')
plt.show()
plt.clf()
