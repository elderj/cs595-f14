import igraph
#print igraph.__version__

g = igraph.Graph()

#34 Members of the club
g.add_vertices(34)

#Connections from the first matrix
g.add_edges([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)])
g.add_edges([(0,10),(0,11),(0,12),(0,13),(0,17),(0,19),(0,21),(0,31)])
g.add_edges([(1,2),(1,3),(1,7),(1,13),(1,17),(1,19),(1,21),(1,30),])
g.add_edges([(2,3),(2,7),(2,8),(2,9),(2,13),(2,27),(2,28),(2,32)])
g.add_edges([(3,7),(3,12),(3,13)])
g.add_edges([(4,6),(4,10)])
g.add_edges([(5,6),(5,10),(5,16)])
g.add_edges([(6,16)])
g.add_edges([(8,30),(8,32),(8,33)])
g.add_edges([(9,33)])
g.add_edges([(13,33)])
g.add_edges([(14,32),(14,33)])
g.add_edges([(15,32),(15,33)])
g.add_edges([(18,32),(18,33)])
g.add_edges([(19,33)])
g.add_edges([(20,32),(20,33)])
g.add_edges([(22,32),(22,33)])
g.add_edges([(23,25),(23,27),(23,29),(23,32),(23,33)])
g.add_edges([(24,25),(24,27),(24,31)])
g.add_edges([(25,31)])
g.add_edges([(26,29),(26,33)])
g.add_edges([(27,33)])
g.add_edges([(28,31),(28,33)])
g.add_edges([(29,32),(29,33)])
g.add_edges([(30,32),(30,33)])
g.add_edges([(31,32),(31,33)])
g.add_edges([(32,33)])




deg = g.degree()
print g
print "Vertex Degree:\n"
print deg



print "\n\nEdge Betweeness:"
print g.community_edge_betweenness()


print "\n\nWalktrap:"
print g.community_walktrap()

print "\n\nFast Greedy:"
print g.community_fastgreedy()
"""
print "\n\nInfoMap:"
print g.community_infomap()
"""


print "\n\nLeading Eigenvectors:"
print g.community_leading_eigenvector(2)
"""
print "\n\nSpinglass"
print g.community_spinglass()
"""


print "\n\nLabel Propagation:"
print g.community_label_propagation()



