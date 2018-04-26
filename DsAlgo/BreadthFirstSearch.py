class node(object):

    def __init__(self, data):
        self.data = data
        self.adjacencylist = []
        self.visited = False
        self.predecessor = None


class Bfs(object):

    def bfs(self, startnode):
        queue = []
        queue.append(startnode)
        startnode.visited = True

        while queue:

            actualnode = queue.pop(0)
            print("%s " % actualnode.data)

            for n in actualnode.adjacencylist:
                if not n.visited:
                    n.visited = True
                    queue.append(n)



#      A
#    B   C
#      D
#        E
node1 = node("A")
node2 = node("B")
node3 = node("C")
node4 = node("D")
node5 = node("E")

node1.adjacencylist.append(node2)
node1.adjacencylist.append(node3)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)

bfsearch = Bfs()
bfsearch.bfs(node1)