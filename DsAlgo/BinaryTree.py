import queue
class node():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


que = queue.queue()


class BinaryTree():
    def __init__(self):
        self.root = None

    def insertlist(self, lst):
        for i in lst:
            self.insert(i)

    def insert(self, cur_val):
        if self.root == None:
            self.root = node(cur_val)
        else:
            self._insert(cur_val, self.root)

    def _insert(self, cur_val, cur_node):
        if cur_val < cur_node.val:
            if cur_node.left == None:
                cur_node.left = node(cur_val)
            else:
                self._insert(cur_val, cur_node.left)
        elif cur_val > cur_node.val:
            if cur_node.right == None:
                cur_node.right = node(cur_val)
            else:
                self._insert(cur_val, cur_node.right)
        else:
            print("Value is in Tree Already")

    def print_tree_in(self):
        if self.root != None:
            self._print_tree_in(self.root)

    def _print_tree_in(self, cur_node):
        if cur_node != None:
            self._print_tree_in(cur_node.left)
            # time.sleep(5)
            print(str(cur_node.val))
            self._print_tree_in(cur_node.right)

    def print_tree_pre(self):
        if self.root != None:
            self._print_tree_pre(self.root)

    def _print_tree_pre(self, cur_node):
        if cur_node != None:
            print(str(cur_node.val))
            self._print_tree_pre(cur_node.left)
            self._print_tree_pre(cur_node.right)
    # Postorder Traversal
    def print_tree_post(self):
        if self.root != None:
            self._print_tree_post(self.root)

    def _print_tree_post(self, cur_node):
        if cur_node != None:
            self._print_tree_post(cur_node.left)
            self._print_tree_post(cur_node.right)
            print(str(cur_node.val))

    # Levelorder Traversal
    """
    def print_tree_level(self):
        if self.root != None:
            var = self.root
            queue.append(var)
            var_l = var.left
            queue.append(var_l)
            var_r = var.right
            queue.append(var_r)
        self._print_tree_level_link(queue)

    def _print_tree_level_link(self, queueNode):
        for i in range(0, len(queueNode) + 1):
            varl = queueNode[i + 1].left
            varr = queueNode[i + 1].right
            if varl != None:
                queueNode.append(varl)
            if varr != None:
                queueNode.append(varr)
                
        for i in range(0, len(queue)):
          print(str(queue[i].val))
    """

    def getMin(self):
        if self.root != None:
            return self._getMin(self.root)

    def _getMin(self, iternode):
        if iternode.left != None:
            return self._getMin(iternode.left)
        else:
            return iternode.val

    def getMax(self):
        if self.root != None:
            return self._getMax(self.root)

    def _getMax(self, iternode):
        if iternode.right != None:
            return self._getMax(iternode.right)
        else:
            return iternode.val

    def traverse_right(self):
        iternode = self.root
        if iternode.right != None:
            print(iternode.val)
            self._traverse_right(iternode.right)

    def _traverse_right(self, cur_node):
        if cur_node != None:
            self._traverse_right(cur_node.left)
            print(str(cur_node.val))
            self._traverse_right(cur_node.right)

    def levelorder(self):
        if self.root != None:
            que.enqueue(self.root)
            while que.getsize() != 0:
                ref = que.dequeue()
                print(ref.val)
                if ref.left != None:
                    #print("-------- "+str(ref.left.val))
                    que.enqueue(ref.left)
                if ref.right != None:
                    #print("-------- " +str(ref.right.val))
                    que.enqueue(ref.right)


#    10
#  5    15
# 2    12
#1   11  13
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(15)
tree.insert(12)
tree.insert(11)
tree.insert(13)
tree.insert(1)
print("Inorder Traversal")
# [2,5,10,11,12]
tree.print_tree_in()
print("Preorder Traversal")
# [10,5,2,11,12]
tree.print_tree_pre()
print("Postorder Traversal")
# [2,11,5,12,10]
tree.print_tree_post()
print("Level Traversal or Breath First Traversal")
tree.levelorder()
print("Get min of Tree")
print(tree.getMin())
print("Get max of Tree")
print(tree.getMax())
print("Right Traversal")
tree.traverse_right()
print("queue length")
print(que.getsize())