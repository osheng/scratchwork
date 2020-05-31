import unittest
from btree import Btree


class Test_Btree(unittest.TestCase):
    def setUp(self):
        self.t1 = Btree(1)
        self.t2 = Btree(2, lnode=self.t1)
        self.t4 = Btree(4)
        self.bst = Btree(3, lnode=self.t2, rnode=self.t4)
        self.non_bst = Btree(3, lnode=self.t2, rnode=Btree(2))

    def test_is_sorted(self):
        self.assertFalse(self.non_bst.is_sorted())
        self.assertTrue(self.t2.is_sorted())
        self.assertTrue(self.bst.is_sorted())

    def test_contains(self):
        self.assertTrue(self.bst.contains(4))
        self.assertFalse(self.bst.contains(-1))


if __name__ == '__main__':
    unittest.main()

# TODO also look up pdb for debugging from commandline
