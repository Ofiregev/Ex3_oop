import json

from DiGraph import Node, Edge, DiGraph


class GraphAlgo:
    def __init__(self):
        self.g = DiGraph()

    def get_graph(self) -> DiGraph:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, Filename: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            f = open(Filename, 'r')
        except IOError:
            return False
        with f as w:
            obj = json.load(w)
            nodes = obj["Nodes"]
            edge = obj["Edges"]
            Nodes = []
            Edges = []
        for n in nodes:
            Nodes.append(Node(n))
        for e in edge:
            Edges.append(Edge(e))
        for i in Nodes:
            self.g.graphDict[i.id] = i
        return True

