import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # 
    def insert(self, value):
        if value < self.value :
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else :
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

