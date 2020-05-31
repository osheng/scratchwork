import unittest
from btree import *


class Test_Btree(unittest.TestCase):
    def setUp(self):
        self.t1 = Btree(1)
        self.t2 = Btree(2, lnode=self.t1)
        self.t4 = Btree(4)
        self.bst = Btree(3, lnode=self.t2, rnode=self.t4)
        self.non_bst = Btree(3, lnode=self.t2, rnode=Btree(2))
        self.utree = Btree(0, rnode=self.bst)

    def test_is_sorted(self):
        self.assertFalse(self.non_bst.is_sorted())
        self.assertTrue(self.t2.is_sorted())
        self.assertTrue(self.bst.is_sorted())

    def test_contains(self):
        self.assertTrue(self.bst.contains(4))
        self.assertFalse(self.bst.contains(-1))

    def test_count_nodes(self):
        self.assertEqual(count_nodes(self.bst), 4)

    def test_is_balanced(self):
        self.assertTrue(self.t1.is_balanced())
        self.assertTrue(self.bst.is_balanced())

    def test_measure_depth(self):
        self.assertEqual(measure_depth(self.t1), 1)
        self.assertEqual(measure_depth(self.bst), 3)

    def test_is_compact(self):
        self.assertFalse(self.utree.is_compact())
        self.assertTrue(self.t4.is_compact())


if __name__ == '__main__':
    unittest.main()

# TODO also look up pdb for debugging from commandline
# To run from commandline call
# python3 -m unittest btree_test.py
