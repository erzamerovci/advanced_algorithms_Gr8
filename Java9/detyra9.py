from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # DFS për të mbushur stack-un
    def dfs1(self, v, visited, stack):
        visited[v] = True
        for n in self.graph[v]:
            if not visited[n]:
                self.dfs1(n, visited, stack)
        stack.append(v)

    # Kthejmë graf-in
    def transpose(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    # DFS për të gjetur komponentët në graf-in e kthyer
    def dfs2(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for n in self.graph[v]:
            if not visited[n]:
                self.dfs2(n, visited, component)

    # Algoritmi i Kosarajut
    def kosaraju(self):
        stack = []
        visited = [False] * self.V

        # 1. DFS për mbledhjen e përfundimeve
        for i in range(self.V):
            if not visited[i]:
                self.dfs1(i, visited, stack)

        # 2. Kthejmë graf-in
        gr = self.transpose()

        # 3. DFS në graf-in e kthyer
        visited = [False] * self.V
        scc_list = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                gr.dfs2(v, visited, component)
                scc_list.append(component)

        return scc_list


# ======================
# Testim
# ======================
g = Graph(6)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(2, 5)
g.add_edge(5, 1)

print("SCC-të:", g.kosaraju())



import itertools

# Lista e brinjëve
edges = [
    (1, 2), (1, 3), (2, 4), (3, 4), (3, 5),
    (4, 6), (5, 6), (6, 7), (7, 8), (7, 9),
    (8, 10), (9, 10)
]

vertices = set()
for u, v in edges:
    vertices.add(u)
    vertices.add(v)

vertices = list(vertices)

def is_vertex_cover(candidate, edges):
    """Kontrollon nëse bashkësia candidate është vertex cover."""
    for u, v in edges:
        if u not in candidate and v not in candidate:
            return False
    return True

def find_min_vertex_cover(vertices, edges):
    """Gjen vertex cover minimal."""
    n = len(vertices)
    for k in range(1, n + 1):  # rrit madhësinë
        for combo in itertools.combinations(vertices, k):
            if is_vertex_cover(combo, edges):
                return combo  # gjetja e parë është minimale

# Testim
solution = find_min_vertex_cover(vertices, edges)
print("Vertex Cover minimal:", solution)
print("Madhesia:", len(solution))
