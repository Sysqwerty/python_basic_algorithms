import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

# {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}
degree_centrality = nx.degree_centrality(G)
# {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}
closeness_centrality = nx.closeness_centrality(G)
# {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}
betweenness_centrality = nx.betweenness_centrality(G)

# Ви також можете знайти найкоротший шлях між двома вузлами або розрахувати середню довжину шляху у графі.
path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333

# Щоб намалювати граф, використовуйте функцію nx.draw().
G = nx.complete_graph(8)
nx.draw(G, with_labels=True)
plt.show()

# Функція nx.complete_graph в бібліотеці NetworkX використовується для створення повного графа. Повний граф — це специфічний тип графа, в якому кожен вузол пов'язаний з кожним іншим вузлом. Іншими словами, між будь-якою парою вузлів існує ребро.
# Тепер розглянемо синтаксис та параметри функції nx.draw, яка використовується для візуалізації графів.
# nx.draw(G, pos=None, ax=None, **kwds)

# 1.  G (обов'язковий): Граф, який потрібно візуалізувати. Це об'єкт графа NetworkX.
# 2. pos (необов'язковий): Словник, який вказує положення вершин. Ключі є вершинами, а значеннями є кортежі з двох координат. Якщо параметр не вказано, буде використано автоматичне розташування вершин.
# 3. ax (необов'язковий): Об'єкт осей Matplotlib, на якому буде намальовано граф. Якщо None, буде використано поточні осі.
# 4. *kwds: Додаткові ключові параметри для керування візуалізацією, такі як колір, стиль лінії, розмір вершин та інші параметри Matplotlib.

# Декілька важливих необов'язкових ключових параметрів **kwds:
# with_labels — логічне значення, яке вказує, чи слід відображати мітки вершин (за замовчуванням True).
# font_weight — вага шрифту для міток вершин ('normal').
# node_color — колір вершин ('blue').
# edge_color — колір ребер ('black').
# node_size — розмір вершин (300).

G1 = nx.complete_graph(4)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G1, **options)
plt.show()

# Розкладка визначає положення вузлів на графіку. Бібліотека networkX має декілька вбудованих розкладок, таких як кругова, випадкова, камеральна тощо.
# Кругова розкладка (circular_layout):
G2 = nx.complete_graph(8)
pos = nx.circular_layout(G2)
nx.draw(G2, pos, with_labels=True)
plt.title("Circular Layout")
plt.show()

# Випадкова розкладка (random_layout):
G3 = nx.complete_graph(8)
pos = nx.random_layout(G3)
nx.draw(G3, pos, with_labels=True)
plt.title("Random Layout")
plt.show()

# Камеральна розкладка (shell_layout):
G4 = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G4, pos)
nx.draw(G4, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()

# У бібліотеці networkx можна візуалізувати графи зі стрілочками для орієнтованих графів. Ці стрілочки показують напрямок ребер в орієнтованому графі.
# Створення орієнтованого графа
DG = nx.DiGraph()
# Додавання ребер
DG.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])
# Малювання графа
pos = nx.spring_layout(DG)
nx.draw(DG, pos, with_labels=True, arrows=True)
plt.show()

# У бібліотеці networkx для реалізації обходу графа в глибину (DFS) та обходу графа в ширину (BFS) вже існують відповідні функції.
# Створення графа
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G5 = nx.Graph(graph)
# DFS
dfs_tree = nx.dfs_tree(G5, source='A')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A
# BFS
bfs_tree = nx.bfs_tree(G5, source='A')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
