#!/usr/bin/env python


# Generates a Graph based on the degree of connection
# between members of the club


"""
Zachary's Karate Club graph

Data file from:
http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm

Reference:
Zachary W. (1977).
An information flow model for conflict and fission in small groups.
Journal of Anthropological Research, 33, 452-473.
"""
import networkx as nx
import matplotlib.pyplot as plt
G=nx.karate_club_graph()
plt.figure(figsize=(8,8))
nx.draw_networkx(G)
plt.axis('off')
#plt.savefig('graph.png')
plt.show()
print("Node Degree")
for v in G:  print('%s %s' % (v,G.degree(v)))

