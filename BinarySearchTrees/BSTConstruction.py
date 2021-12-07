class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution1(BST):

    def insert(self, value):
        """
        Average (balanced tree):
        O(logn) time
        O(1) space

        Worst (highly skewed):
        O(n) time
        O(1) space

        n is the number of the nodes
        """
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right

        return self

    def contains(self, value) -> bool:
        """
        Average:
        O(logn) time
        O(1) space

        Worst:
        O(n) time
        O(1) space

        n is the number of the nodes
        """
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def remove(self, value, parent=None):
        """
        Average:
        O(logn) time
        O(1) space

        Worst:
        O(n) time
        O(1) space

        n is the number of the nodes
        """
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left is not None and current.right is not None:
                    current.value = self.right.get_min()
                    self.right.remove(value=current.value, parent=current)
                # Root node has no parent node
                elif parent is None:
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        pass
                elif parent.left == current:
                    if current.left is not None:
                        parent.left = current.left
                    else:
                        parent.left = current.right
                elif parent.right == current:
                    if current.left is not None:
                        parent.right = current.left
                    else:
                        parent.right = current.right
                break

        return self

    def get_min(self) -> int:
        current = self
        while current is not None:
            current = current.left

        return current.value


class Solution2(BST):

    def insert(self, value):
        """
        Average:
        O(logn) time
        O(logn) space

        Worst:
        O(n) time
        O(n) space

        n is the number of the nodes
        """
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def contains(self, value) -> bool:
        """
        Average:
        O(logn) time
        O(logn) space

        Worst:
        O(n) time
        O(n) space

        n is the number of the nodes
        """
        if value < self.value:
            if self.left is not None:
                return self.left.contains(value)
            else:
                return False
        elif value > self.value:
            if self.right is not None:
                return self.right.contains(value)
            else:
                return False
        else:
            return True

    def remove(self, value, parent=None):
        """
        Average:
        O(logn) time
        O(logn) space

        Worst:
        O(n) time
        O(n) space

        n is the number of the nodes
        """
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, parent=self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, parent=self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min()
                self.right.remove(value=self.value, parent=self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                if self.left is not None:
                    parent.left = self.left
                else:
                    parent.left = self.right
            elif parent.right == self:
                if self.left is not None:
                    parent.right = self.left
                else:
                    parent.right = self.right

        return self

    def get_min(self) -> int:
        if self.left is not None:
            return self.left.get_min()
        else:
            return self.value
