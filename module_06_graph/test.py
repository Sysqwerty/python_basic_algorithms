import networkx as nx
import matplotlib.pyplot as plt

# Розглянемо граф із вершинами A, B, C, D та ребрами (A, B), (B, C), (C, D), (D, A).

# Матриця суміжності
adj_matrix = [
    [0, 1, 0, 1],  # Вершина A
    [1, 0, 1, 0],  # Вершина B
    [0, 1, 0, 1],  # Вершина C
    [1, 0, 1, 0]   # Вершина D
]

# # Створюємо порожній граф
# G = nx.Graph()
# # Додаємо вершини
# G.add_nodes_from(["A", "B", "C", "D"])
# # Додаємо ребра
# G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")])
# # Задаємо розташування вершин
# positions = {
#     "A": (0, 1),
#     "B": (1, 1),
#     "C": (1, 0),
#     "D": (0, 0)
# }
# # Малюємо граф
# plt.figure(figsize=(6, 6))
# nx.draw_networkx(G, pos=positions, with_labels=True,
#                  font_weight='bold', node_color='lightblue', edge_color='gray')
# plt.axis("off")
# plt.show()


def is_edge(arr, v1, v2):
    return arr[v1][v2] if arr[v1][v2] else -1


if __name__ == "__main__":
    print(is_edge(adj_matrix, 2, 3))
