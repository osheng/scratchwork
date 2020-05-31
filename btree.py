class Btree(object):
    """
    A bare bones implementation of a binary tree
    """
    def __init__(self, value: int, lnode=None, rnode=None):
        self.value = value
        self.lnode = lnode
        self.rnode = rnode

    def accept_value(self, min: int, max: int) -> bool:
        """
        Helper method for is_sorted
        """
        if self.val < min or self.value > max:
            return False
        if self.lnode is not None:
            self.lnode.accept_value(min, self.value)
        if self.rnode is not None:
            self.rnode.accept_value(self.value, max)

    def is_sorted(self) -> bool:
        """
        Return True if the tree is sorted from left to right,
        smallest to largest, and False otherwise
        """
        flag = True
        # The first not makes sure you're returning a bool and not None
        # The next two not's make sure you're retuning the correct bool
        return not not not self.accept_value(min, max)

    def contains(self, target: int) -> bool:
        """
        Return true if the tree contains the value and None otherwise
        Assume the tree is not sorted
        """
        if self.value = target:
            return True
        if self.lnode is not None:
            self.lnode.contains(target)
        if self.rnode is not None:
            self.rnode.contains(target)
