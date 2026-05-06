
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi Yükle
df = pd.read_csv('data/network_data.csv')

# 2. Çizgeyi (Graph) Oluştur
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'], weight=row['Distance_km'])

# 3. En Kısa Yolu Hesapla (Dijkstra)
source_node = 'Tuzla'
target_node = 'Beşiktaş'
shortest_path = nx.shortest_path(G, source=source_node, target=target_node, weight='weight')
shortest_distance = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')

print(f"{source_node} -> {target_node} arası en kısa yol: {shortest_path}")
print(f"Toplam Mesafe: {shortest_distance} km")

# 4. Görselleştirme
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 7))

# Tüm düğümler ve kenarlar
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# En kısa yolu kırmızıyla işaretle
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=3)

plt.title(f"E-ticaret Lojistik Ağı Optimizasyonu\n{source_node} - {target_node} En Kısa Yol")
plt.savefig('network_visualization.png')
plt.show()
