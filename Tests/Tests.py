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
        self.assertIsNone(g.graphDict.get(1))

if __name__ == '__main__':
    unittest.main()
