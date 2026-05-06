import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMapAirport = {}
        self._airports = DAO.getAllAirports()
        for air in self._airports:
            self._idMapAirport[air.ID] = air

    def buildGraph(self, d_min):
        # Funzione per creare il grafo. Devo aggiungere i nodi e gli archi
        # Dato che devo mettere solamente gli areoporti collegati da almeno un volo
        # come nodi, aggiungo archi e nodi insieme, perchè networkx aggiunge nodi in automatico
        # quando chiamo la funzione per aggiungere archi.
        # Devo prima fare un eventuale media tra le distanze degli archi A -> B e B -> A
        self._graph.clear()
        self._addEdges(d_min)

    def _addEdges(self, d_min):
        allEdges = DAO.getEdges()
        for edge in allEdges:
            u = edge[0]
            v = edge[1]
            peso = edge[2]
            if peso > d_min:
                self._graph.add_edge(self._idMapAirport.get(u), self._idMapAirport.get(v), weight=peso)

    def get_num_nodi(self):
        return len(self._graph.nodes)

    def get_num_edges(self):
        return len(self._graph.edges)

    def get_all_archi(self) -> str:
        result = ""
        for u, v, attrs in self._graph.edges(data=True):
            result += f"{u} <-> {v} | Distanza media: {attrs["weight"]:.2f} miglia.\n"
        return result