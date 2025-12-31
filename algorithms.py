import networkx as nx

# --- Paramètres alpha et beta ---
alpha = 1   # tu peux changer
beta = 10    # tu peux changer

# --- Définition des arcs avec couples de poids (w1, w2) ---
edges = [
    ("Source", "A", (10, 2)),
    ("Source", "B", (50, 1)),
    ("Source", "C", (20, 5)),

    ("A", "D", (10, 2)),
    ("A", "E", (30, 8)),

    ("B", "D", (20, 1)),
    ("B", "F", (100, 1)),

    ("C", "E", (10, 5)),

    ("D", "Dest", (40, 2)),
    ("D", "E", (10, 3)),

    ("E", "Dest", (10, 9)),
    ("F", "Dest", (10, 1))
]

# --- Création du graphe orienté ---
G = nx.DiGraph()
for u, v, (w1, w2) in edges:
    combined_weight = alpha * w1 + beta * w2
    G.add_edge(u, v, cost=combined_weight)

# --- Liste des sommets ---
nodes = list(G.nodes)

# --- Initialisation de la matrice de distances et prédécesseurs ---
dist = {u: {v: float('inf') for v in nodes} for u in nodes}
pred = {u: {v: None for v in nodes} for u in nodes}

for u in nodes:
    dist[u][u] = 0
for u, v, data in G.edges(data=True):
    dist[u][v] = data['cost']
    pred[u][v] = u

# --- Algorithme Floyd-Warshall ---
for k in nodes:
    for i in nodes:
        for j in nodes:
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                pred[i][j] = pred[k][j]

# --- Fonction pour reconstruire le chemin le plus court ---
def get_path(pred, source, dest):
    path = []
    if pred[source][dest] is None:
        return None  
    current = dest
    while current != source:
        path.append(current)
        current = pred[source][current]
    path.append(source)
    path.reverse()
    return path

# --- Exemple : plus court chemin Source -> Dest ---
source = "Source"
dest = "Dest"
path = get_path(pred, source, dest)
distance = dist[source][dest]

print("Poids combinés : alpha =", alpha, ", beta =", beta)
print("Chemin le plus court de", source, "à", dest, ":", path)
print("Distance totale :", distance)