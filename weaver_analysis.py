import networkx as nx
import pickle5 as pickle


def gui_paths(G: nx.Graph, s1: str, s2: str):
    paths = list(nx.all_shortest_paths(G, s1, s2))
    print("#"*20)
    print(f'Showing the possible (fastest) paths between "{s1}" and "{s2}"')
    print(f'Optimal path length: {len(paths[0])} (optimal number of steps therefore {len(paths[0]) -1})')
    for i, p in enumerate(paths): 
        print(f"path {i+1}: "+ " -> ".join(p))
    print("#"*20)


def gui_paths_4(s1: str, s2:str):
    with open('weaver-graph-4.pkl', 'rb') as f:
        G4 = pickle.load(f)
    gui_paths(G4, s1, s2)


def gui_paths_5(s1: str, s2:str):
    with open('weaver-graph-5.pkl', 'rb') as f:
        G5 = pickle.load(f)
    gui_paths(G5, s1, s2)
