from time import time
from model.model import Model

model = Model()

start_time = time()
model.buildGraph(1000)
end_time = time()

print("Grafo correttamente creato!")
print(f"Il grafo ha {model.get_num_nodi()} nodi e {model.get_num_edges()} archi.")
for u, v, w in model._graph.edges(data=True):
    print(f"Primo aeroporto: {u} | Secondo aeroporto: {v} | Peso: {w["weight"]}")