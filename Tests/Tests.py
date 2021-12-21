import unittest
import DiGraph
import GraphAlgo
import src


class Test_read_from_file(unittest.TestCase):
    def test_add(self):
        g = DiGraph.DiGraph()
        c = g.add_node(1,("2","2","2"))
        cc = g.add_node(1,("2","2","3"))
        self.assertFalse(cc)
        v = g.graphDict[1]
        self.assertEqual(g.graphDict[1], v)

    # def read_from_json(self):

    def test_remove_node(self):
        g = DiGraph.DiGraph()
        self.assertFalse(g.remove_node(1))
        c = g.add_node(1, ("2", "2", "2"))
        self.assertTrue(g.remove_node(1))
        self.assertIsNone(g.graphDict.get(3))

    def test_add_Edge(self):
        g = DiGraph.DiGraph()
        g.add_node(2, ("3", "3", "0"))
        g.add_node(1, ("3", "3", "0"))
        self.assertTrue(g.add_edge(1,2,5.4))

    def test_remove_Edge(self):
        g = DiGraph.DiGraph()
        g.add_node(2, ("3", "3", "0"))
        g.add_node(1, ("3", "3", "0"))
        g.add_edge(1, 2, 5.4)
        self.assertTrue(g.remove_edge(1, 2))
        g.add_edge(1, 2, 5.4)
        del (g.graphDict.get(1).outEdge)[2]
        self.assertFalse(g.remove_edge(1,2))

    def test_in_edge(self):
        g = DiGraph.DiGraph()
        g.add_node(1, ("3", "3", "0"))
        g.add_node(2, ("3", "3", "0"))
        g.add_node(3, ("3", "3", "0"))
        g.add_edge(1,2,77)
        g.add_edge(2,1,44)
        g.add_edge(3,1,27)
        g.add_edge(3,2,27)
        self.assertEqual(g.all_in_edges_of_node(1),{2:44,3:27})
        self.assertEqual(g.all_out_edges_of_node(3),{1:27,2:27})

    def test_loadFrom_json(self):
        g= GraphAlgo.GraphAlgo()
        file ='../data/A5.json'
        b = g.load_from_json(file)
        self.assertTrue(b)

    def test_iterationExsemple(self):
        g = GraphAlgo.GraphAlgo()
        file = '../data/A0.json'
        b = g.load_from_json(file)
        # nd =[]
        # ed =[]
        # count =0
        # for key in g.g.graphDict.keys():
        #     nd.append({"id": key ,
        #                "pos":g.g.graphDict[key].pos})
        #     for e in g.g.graphDict[key].outEdge:
        #         ed.append({"src":key ,"w":g.g.graphDict[key].outEdge[e] , "dest": e})
        self.assertTrue(True, "this is an iterator Example")

    def test_getEdgeBySrc(self):
        g = DiGraph.DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1,2,11)
        g.add_edge(1,3,12)
        g.add_edge(1,4,12)
        g.add_edge(2,1,23)
        list = [2,3,4]
        self.assertEqual(list, g.getEdgeBySrc(1))

    def test_getweightbysrc(self):
        g = DiGraph.DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 11)
        g.add_edge(1, 3, 12)
        g.add_edge(1, 4, 12)
        g.add_edge(2, 1, 23)
        self.assertEqual(11, g.getWeightOfEdge(1, 2))
        self.assertEqual(23, g.getWeightOfEdge(2, 1))

    def test_shortest_path(self):
        d = GraphAlgo.GraphAlgo()
        g = d.g
        g.add_node(0, ("1", "2", "2"))
        g.add_node(1, ("1", "2", "2"))
        g.add_node(2, ("1", "2", "2"))

        g.add_edge(2, 1, 3)
        g.add_edge(0, 1, 8)
        g.add_edge(0, 2, 1)
        g.add_edge(1, 2, 4)
        self.assertEqual([4, [0, 2, 1]], d.shortest_path(0, 1))
        self.assertEqual([float('inf'), []], d.shortest_path(1, 4))


if __name__ == '__main__':
    unittest.main()
