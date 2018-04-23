class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curnode):
        if data < curnode.data:
            if curnode.left != None:
                self._insert(data, curnode.left)
            else:
                curnode.left = node(data)
        elif data > curnode.data:
            if curnode.right != None:
                self._insert(data, curnode.right)
            else:
                curnode.right = node(data)
        else:
            print("{} already in the Tree".format(data))

    def traverse_in(self):
        iternode = self.root
        if iternode != None:
            self._traverse_in(iternode)

    def _traverse_in(self, curnode):
        if curnode != None:
            self._traverse_in(curnode.left)
            print(curnode.data)
            self._traverse_in(curnode.right)

#     10
#   5    16
# 2    12
btree = BinaryTree()

btree.insert(10)
btree.insert(5)
btree.insert(2)
btree.insert(16)
btree.insert(12)

print(btree.traverse_in())