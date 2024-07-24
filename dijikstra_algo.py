import matplotlib.pyplot as plt
import networkx as nx
import heapq

# Function to create the graph based on user input
def create_graph():
    g = nx.Graph()
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (node1 node2 weight): ").split())
        g.add_edge(u, v, weight=weight)
    return g

# Implement Dijkstra's algorithm
def dijkstra(gr, src):
    # Priority queue to store the minimum distance and node
    q = [(0, src)]
    dist = {node: float('infinity') for node in gr.nodes}
    prev = {node: None for node in gr.nodes}
    dist[src] = 0
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        # If the distance of the current node is greater than the stored distance, continue
        if cur_dist > dist[cur_node]:
            continue
        for nbr, wt in gr[cur_node].items():
            new_dist = cur_dist + wt['weight']
            # Update distance and previous node if shorter path found
            if new_dist < dist[nbr]:
                dist[nbr] = new_dist
                prev[nbr] = cur_node
                heapq.heappush(q, (new_dist, nbr))
    return dist, prev

def find_shortest_path(gr, src, tgt):
    dist, prev = dijkstra(gr, src)
    path = []
    cur = tgt
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path

# Create the graph based on user input
g = create_graph()

# Get user input for source and target nodes
try:
    src = int(input("Enter the source node: "))
    tgt = int(input("Enter the target node: "))
    if src not in g.nodes or tgt not in g.nodes:
        raise ValueError("Nodes must be in the graph.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Find the shortest path from the source to the target node
path = find_shortest_path(g, src, tgt)
print(f"The shortest path from node {src} to node {tgt} is: {path}")

# Highlight the shortest path
path_edges = list(zip(path, path[1:]))

# Draw the graph with the shortest path highlighted
plt.figure(figsize=(8, 6))
pos = nx.circular_layout(g)
nx.draw(g, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=15)
nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r', width=2)
plt.title(f'Shortest Path ({src} to {tgt})')
plt.show()
