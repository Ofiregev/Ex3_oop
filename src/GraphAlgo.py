import json
from math import inf
import queue

from DiGraph import Node, Edge, DiGraph


class GraphAlgo:
    def __init__(self):
        self.g = DiGraph()
        self.D ={}
        self.nodeQ = []
        self.black = []
        self.parent = {}
        # self.D[1] ={}
        # self.D["max"] = -inf


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

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        raise NotImplementedError

    def Dijkstra(self,src :int):
        for i in self.g.graphDict:
            if i == src:
                self.nodeQ.append({"id":src,"w":0})
            else:
                self.nodeQ.append({"id":i,"w":inf})
        while len(self.black) != len(self.g.graphDict):
            if self.nodeQ.__len__() == 0:
                return
            self.nodeQ = sorted(self.nodeQ, key=lambda i: i['w'])
            v = self.nodeQ.pop(0)
            nei = self.g.getEdgeBySrc(v)
            # for i in nei:
            #     relax(v,i)

            # dict(sorted(x.items(), key=lambda item: item[1]))
            # v = self.nodeQ.
            # if self.black.count(v):
            #     continue
            # self.black.append(v)
            # nei = self.g.getEdgeBySrc(v)
            # for i in nei:
            #     relax(v,t)


    # def relax(self,v,t):
    #     if self.nodeQ
    #

def main():
    d=GraphAlgo()
    g = d.g

    # file ='../data/A5.json'
    # g.load_from_json(file)
    print(g.add_node(2, ("3", "3", "0")))
    print(g.add_node(1, ("3", "3", "0")))
    print(g.add_node(3, ("3", "3", "0")))

    print(g.add_edge(1, 2, 5.4))
    print(g.add_edge(3, 1, 5.4))
    print(g.add_edge(1, 3, 5.4))
    print(g.getEdgeBySrc(1))
    print(GraphAlgo.Dijkstra(d,1))


    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(2))


if __name__ == '__main__':
    main()
