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

    # TODO write an insert method and array_to_tree
