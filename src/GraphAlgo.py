import copy
import json
import time
from math import inf
import queue
from tkinter import Tk

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
            self.g.add_node(i.id,i.pos)
        for i in Edges:
            self.g.add_edge(i.src,i.dest,i.w)

        return True

    def save_to_json(self, file_name: str) -> bool:
        nd =[]
        ed =[]
        for key in self.g.graphDict.keys():
            nd.append({"id": key ,
                       "pos":self.g.graphDict[key].pos})
            for e in self.g.graphDict[key].outEdge:
                ed.append({"src":key ,"w":self.g.graphDict[key].outEdge[e] , "dest": e})
        dic = {}
        dic["Nodes"] = nd
        dic["Edges"] = ed
        json_object = json.dumps(dic)
        try:
            f = open(file_name , 'w')
        except IOError:
            return False
        with f as outFile:
            outFile.write(json_object)
        return True
    def TSP(self, node_lst: list[int]) -> (list[int], float):
        min =inf
        """this is the Global min for all the permutations"""
        lst =[]
        """this lst will represent the most better permutation of the list"""
        for i in node_lst:
            """checking when every node is the beginning of the circle what is the most good permutation"""
            temp = self.find_way(copy.deepcopy(node_lst), i)
            if temp[1] <= min:
                min = temp[1]
                lst =temp [0]
                print(temp)
        return [lst, min]

    def find_way(self, lst:list ,start:int):
        per =[]
        per.append(start)
        lst.remove(start)
        index = 0
        w = 0
        nex = start
        while lst:
            self.Dijkstra(nex)
            min = self.D.get(lst[0])
            for e in lst:
                if self.D.get(e) <= min:
                    min = self.D.get(e)
                    index = e
            nex = index
            lst.remove(nex)
            per.append(nex)
            w += min
        per.append(start)
        self.Dijkstra(nex)
        print(start,self.D.get(start))
        w += self.D.get(start)

        return [per,w]



    def Dijkstra(self,src :int):
        self.D = {}
        self.nodeQ = []
        self.black = []
        self.parent = {}
        self.D["maxPath"] = float(-inf)
        for i in self.g.graphDict:
            if i == src:
                self.nodeQ.append({"id":src,"w":0})
                self.D[src] = 0
                self.parent[src] =-1
            else:
                self.D[i] = inf ##save in a dictinury the nodes w ,this is good bebause its by key
        while len(self.black) != len(self.g.graphDict):
            if self.nodeQ.__len__() == 0:
                return
            self.nodeQ = sorted(self.nodeQ, key=lambda i: i['w'])
            v = self.nodeQ.pop(0)['id']
            if(self.black.__contains__(v)):
                continue
            self.black.append(v)
            nei = self.g.getEdgeBySrc(v)
            for i in nei:
                 self.relax(v, i)
        for i in self.g.graphDict:
            if self.D[i] > self.D["maxPath"]:
                self.D["maxPath"] = self.D[i]



    def relax(self,v,t):
        curr_w = self.D[v] + self.g.getWeightOfEdge(v, t)
        if self.D[t] > float(curr_w):
            self.D[t] = float(curr_w)
            self.parent[t] = v
            self.nodeQ.append({"id": t, "w": curr_w})


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.g.graphDict.get(id2) is None or self.g.graphDict.get(id1) is None:
            list =[]
            list.append(float('inf'))
            list.append([])
            return list
        self.Dijkstra(id1)
        list1 = []
        list2 = []
        list1.append(self.D[id2])
        list2.append(id1)
        i = id2
        while (i != -1 and self.parent.get(i)!=-1):
            t = self.parent.get(i)
            list2.append(t)
            i = self.parent[t]
        list2.append(id2)
        list1.append(list2)
        return list1

    def centerPoint(self) -> (int, float):
        MAXLIST = {}
        minMaxPath = float(inf)
        node_id = -1
        for i in self.g.graphDict.keys():
            self.Dijkstra(i)
            MAXLIST[i] = self.D.get("maxPath")
            if self.D.get("maxPath") < minMaxPath:
                minMaxPath = self.D.get("maxPath")
                node_id = i
        list = []
        list.append(node_id)
        list.append(minMaxPath)
        print(MAXLIST)
        print(MAXLIST.get(362))
        return list

    def plot_graph(self) -> None:
        startG();



def main():
    g = GraphAlgo()
    g.plot_graph()
    # file = '../data/A0.json'
    # g.load_from_json(file)
    # g.Dijkstra(1)

    d=GraphAlgo()
    #
    file ='../data/A5.json'
    d.load_from_json(file)
    d.shortest_path(0,1)
    start = time.time()
    print("The center of", file, " graph is:",d.centerPoint(), "ofir hamalka regev")
    end = time.time()
    print(end-start)
    # print(g.add_node(2, ("3", "3", "0")))
    # print(g.add_node(1, ("3", "3", "0")))
    # print(g.add_node(3, ("3", "3", "0")))
    #
    # print(g.add_edge(1, 2, 5.4))
    # print(g.add_edge(3, 1, 5.4))
    # print(g.add_edge(1, 3, 5.4))

    # print(g.getEdgeBySrc(1))
    # print(GraphAlgo.Dijkstra(d,1))


    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(2))


if __name__ == '__main__':
    main()
