from math import ceil, log


class Btree(object):
    """
    A bare bones implementation of a binary tree
    """

    def __init__(self, value: int, lnode=None, rnode=None):
        self.value = value
        self.lnode = lnode
        self.rnode = rnode

    def is_sorted(self) -> bool:
        """
        Return True if the tree is sorted from left to right,
        smallest to largest, and False otherwise
        """
        def accept(self, min_val=None, max_val=None) -> bool:
            """
            Helper function for is sorted
            """
            if self is None:
                return True
            if (min_val is not None and self.value < min_val) or \
                    (max_val is not None and self.value > max_val):
                # print("failed at {}. min was {}. max was {}".\
                # format(self.value, min_val, max_val))
                return False
            return accept(self.lnode, min_val, self.value) and\
                accept(self.rnode, self.value, max_val)

        return accept(self)

    def contains(self, target: int) -> bool:
        """
        Return true if the tree contains the value and None otherwise
        Assume the tree is not sorted
        """
        if self.value == target:
            return True
        return (self.lnode is not None and self.lnode.contains(target)) or \
            (self.rnode is not None and self.rnode.contains(target))

    def is_balanced(self) -> bool:
        """
        Return whether the Btree is balanced
        """
        return 0 <= count_nodes(self.lnode) - count_nodes(self.rnode) <= 1

    def is_compact(self) -> bool:
        """
        Return whether self is compact
        """
        return measure_depth(self) <= log(count_nodes(self) + 1, 2)


def count_nodes(t: Btree) -> int:
    """
    Return the number of nodes in a Btree
    """
    if t is None:
        return 0
    return count_nodes(t.lnode) + count_nodes(t.rnode) + 1


def measure_depth(t: Btree) -> int:
    if t is None:
        return 0
    return 1 + max(measure_depth(t.lnode), measure_depth(t.rnode))

# TODO write an insert method and array_to_tree
