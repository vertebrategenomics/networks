# Import libraries
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Network setup
graph_type = nx.Graph()
df = pd.read_csv('/Users/jairtorres/Desktop/DGN.csv')
G = nx.from_pandas_edgelist(df, create_using=graph_type)

# Draw network
nx.draw(G)
plt.show()

# Define bipartite graph
for _, row in df.iterrows():
    G.add_node(row['source'], bipartite=0)
    G.add_node(row['target'], bipartite=1)
    G.add_edge(row['source'], row['target'])

# Apply Louvain algorithm for community detection
communities = list(nx.community.louvain_communities(G, seed=123))
print(communities)

# Sort communities by size
community_sizes = [(i, len(community)) for i, community in enumerate(communities)]
sorted_communities = sorted(community_sizes, key=lambda x: x[1], reverse=True)

print("Largest to smallest:")
for community_id, size in sorted_communities:
    print(f"Community {community_id + 1}: {len(communities[community_id])} nodes")

# Set up and draw community 14
community_14 = communities[13]
subgraph_community_14 = G.subgraph(community_14)
pos = nx.spring_layout(subgraph_community_14, seed=123)

plt.figure(figsize=(12, 10))
nx.draw(
    subgraph_community_14,
    pos,
    with_labels=True,
    node_color='red',
    font_weight='bold',
    node_size=500,
    width=1.0
)

# Apply Kamada-Kawai layout
pos = nx.kamada_kawai_layout(subgraph_community_14)
plt.figure(figsize=(15, 12))
nx.draw(
    subgraph_community_14,
    pos,
    with_labels=True,
    node_size=500,
    node_color='red',
    font_weight='bold'
)
plt.show()
