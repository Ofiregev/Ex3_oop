import unittest
import Graph
import src


class Test_read_from_file(unittest.TestCase):
    def test_add(self):
        g = Graph.Digraph()
        c = g.add_node(1,("2","2","2"))
        cc = g.add_node(1,("2","2","3"))
        self.assertFalse(cc)
        v = g.graphDict[1]
        self.assertEqual(g.graphDict[1], v)

    # def read_from_json(self):

    def test_remove_node(self):
        g = Graph.Digraph()
        self.assertFalse(g.remove_node(1))
        c = g.add_node(1, ("2", "2", "2"))
        self.assertTrue(g.remove_node(1))
        self.assertIsNone(g.graphDict.get(3))

    def test_add_Edge(self):
        g = Graph.Digraph()
        g.add_node(2, ("3", "3", "0"))
        g.add_node(1, ("3", "3", "0"))
        self.assertTrue(g.add_edge(1,2,5.4))

    def test_remove_Edge(self):
        g = Graph.Digraph()
        g.add_node(2, ("3", "3", "0"))
        g.add_node(1, ("3", "3", "0"))
        g.add_edge(1, 2, 5.4)
        self.assertTrue(g.remove_edge(1, 2))
        g.add_edge(1, 2, 5.4)
        del (g.graphDict.get(1).outEdge)[2]
        self.assertFalse(g.remove_edge(1,2))

    def test_in_edge(self):
        g = Graph.Digraph()
        g.add_node(1, ("3", "3", "0"))
        g.add_node(2, ("3", "3", "0"))
        g.add_node(3, ("3", "3", "0"))
        g.add_edge(1,2,77)
        g.add_edge(2,1,44)
        g.add_edge(3,1,27)
        g.add_edge(3,2,27)
        self.assertEqual(g.all_in_edges_of_node(1),{2:44,3:27})
        self.assertEqual(g.all_out_edges_of_node(3),{1:27,2:27})



if __name__ == '__main__':
    unittest.main()
