# networks.py

import random
import networkx as nx

def create_hierarchical_network(num_levels, span_of_control):
    """
    Creates a hierarchical (tree-like) organizational network.
    """
    G = nx.DiGraph()
    current_id = 0
    G.add_node(current_id)
    previous_level = [current_id]
    current_id += 1

    for level in range(1, num_levels):
        current_level = []
        for manager in previous_level:
            for _ in range(span_of_control):
                G.add_node(current_id)
                G.add_edge(manager, current_id)
                current_level.append(current_id)
                current_id += 1
        previous_level = current_level

    return G

def create_onion_network(num_levels, span_of_control):
    """
    Creates an onion-like hierarchical network with additional inter-layer connections.
    """
    G = nx.DiGraph()
    current_id = 0
    G.add_node(current_id)
    previous_level = [current_id]
    current_id += 1

    for level in range(1, num_levels):
        current_level = []
        for manager in previous_level:
            for _ in range(span_of_control):
                G.add_node(current_id)
                G.add_edge(manager, current_id)
                current_level.append(current_id)
                current_id += 1
        # Add inter-layer (lateral) connections
        for node in current_level:
            if random.random() < 0.3:  # 30% chance to connect laterally
                lateral = random.choice(previous_level)
                if lateral != node:
                    G.add_edge(node, lateral)
        previous_level = current_level

    return G

def create_small_world_network(num_nodes, k, p):
    """
    Creates a Small-World network for social interactions.
    """
    return nx.watts_strogatz_graph(num_nodes, k, p)

def create_scale_free_network(num_nodes, m):
    """
    Creates a Scale-Free network for social interactions.
    """
    return nx.barabasi_albert_graph(num_nodes, m)

def add_random_edges(G, num_edges):
    """
    Dynamically adds random edges to a network.
    """
    possible_edges = list(nx.non_edges(G))
    random.shuffle(possible_edges)
    added = 0
    for edge in possible_edges:
        if added >= num_edges:
            break
        G.add_edge(*edge)
        added += 1

def remove_random_edges(G, num_edges):
    """
    Dynamically removes random edges from a network.
    """
    existing_edges = list(G.edges())
    random.shuffle(existing_edges)
    removed = 0
    for edge in existing_edges:
        if removed >= num_edges:
            break
        G.remove_edge(*edge)
        removed += 1
