import json
import string


class Digraph():
    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.graphDict = {}

def load_from_json(self, Filename:string):
    with open(Filename, 'r') as w:
        obj = json.load(w)
        nodes = obj["Nodes"]
        edge = obj["Edges"]
    for n in nodes:
        self.Nodes.append(Node(n))
    for e in edge:
        self.Edges.append(Edge(e))
    for i in self.Node:
        self.graphDict[i.id] = i
    print(dict(self.graphDict))

def v_size(self) -> int:
    return self.Nodes.length


def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        raise NotImplementedError

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        raise NotImplementedError

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        raise NotImplementedError

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedErro

class Node:
    def __init__(self,list):
        self.id = list["id"]
        self.pos = list["pos"]

    def __repr__(self):
        return f"(node id: {self.id} node pos: {self.pos})"

    def __str__(self):
        return f"(node id: {self.id} node pos: {self.pos})"


class Edge:
    def __init__(self, list):
        self.src = list["src"]
        self.w = list["w"]
        self.dest = list["dest"]

    def __repr__(self):
        return f"src: {self.src} dst: {self.dest} wight: {self.w}"

    def __str__(self):
        return f"src: {self.src} dst: {self.dest} wight: {self.w}"


def main():
    g = Digraph()
    file ='../data/A5.json'
    load_from_json(g,file)


if __name__ == '__main__':
    main()

