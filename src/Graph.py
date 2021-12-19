import json
import string


class Digraph():
    def __init__(self):
        self.graphDict = {} #{key :node_id, value: node_data}
        self.mc = 0

    def load_from_json(self, Filename:string):
        with open(Filename, 'r') as w:
            obj = json.load(w)
            nodes = obj["Nodes"]
            edge = obj["Edges"]
            Nodes =[]
            Edges =[]
        for n in nodes:
            Nodes.append(Node(n))
        for e in edge:
            Edges.append(Edge(e))
        for i in Nodes:
            self.graphDict[i.id] = i


    def v_size(self) -> int:
        return self.Nodes.__len__()

    def e_size(self) -> int:
        return self.Edges.__len__()

    def get_all_v(self) -> dict:
        return self.graphDict

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def get_mc(self) -> int:

        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: 
         will do nothing
        """
        raise NotImplementedError

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.graphDict.get(node_id) != None:
            return False
        list ={}
        str = pos[0]
        for st in pos[1:]:
            str+="," +st
        list["id"] = node_id
        list["pos"] =str
        node = Node(list)
        self.graphDict[node_id] = node
        return True


    def remove_node(self, node_id: int) -> bool:
        if self.graphDict.__contains__(node_id):
            self.graphDict.pop(node_id)
            return True
        return False
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
    #
    # def remove_edge(self, node_id1: int, node_id2: int) -> bool:
    #     """
    #     Removes an edge from the graph.
    #     @param node_id1: The start node of the edge
    #     @param node_id2: The end node of the edge
    #     @return: True if the edge was removed successfully, False o.w.
    #     Note: If such an edge does not exists the function will do nothing
    #     """
    #     raise NotImplementedErro

class Node:
    def __init__(self,list):
        self.id = list["id"]
        self.pos = list["pos"]
        self.inEdge ={}  #this is dic of edge into our node <"other nide.id",w>
        self.outEdge ={} #this is dic of edge from our node <"other nide.id",w>

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
    # file ='../data/A5.json'
    # g.load_from_json(file)
    print(g.add_node(2, ("3","3","0")))
    print(g.add_node(1, ("3","3","0")))
    print(g.remove_node(1))
    print(g.remove_node(1))



if __name__ == '__main__':
    main()

