#Header information


import networkx as nx
import matplotlib.pyplot as plt 

def RegularLattice(nodes, k, display_edges=False):
    grh= nx.Graph()
    for i in range(nodes):
        for j in range(1,k+1):
            grh.add_edge(i,(i+j)%nodes)
    nx.draw(grh,with_labels=True)
    # OPTIONAL PARAMETER: Displays adjacency aesthetically if verification for edges is necessary
    if display_edges:
        print("\n".join([str((n, nbrdict)) for n, nbrdict in grh.adjacency()]))

if __name__ == '__main__':

    RegularLattice(50,3)

