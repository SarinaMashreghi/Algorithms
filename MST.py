#finding the minimum spanning tree of a weighted graph

import networkx as nx
import random

def create_random_graph(v, e, min_v=5, max_v=10, max_e=20, max_w=10):
    
    G = nx.Graph()
    num_v = random.randint(min_v, max_v)
    for i in range(1, num_v+1):
        G.add_node(i)
        
    #create random weighted edges
    num_e = random.randint(v, max_e)
    all_edges = []
    while(len(all_edges)<num_e):
        e1 = random.choice(list(range(1, v+1)))
        e2 = random.choice(list(range(1, v+1)).remove(e1))
        if not((e1, e2) in all_edges):
            all_edges.append((e1, e2))
            
    weighted_edges = []
    for i in range(num_e):
        w = random.randint(1, max_w)
        weighted_edges.append((all_edges[i][0], all_edges[i][1], w))
        
    G.add_weighted_edges_from(weighted_edges)
    
    return G

g = create_random_graph(5, 10)
nx.draw(g, with_labels=True)            
    
    