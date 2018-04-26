class node(object):

    def __init__(self, data):
        self.data = data
        self.adjacencylist = []
        self.visited = False
        self.predecessor = None


class Dfs(object):

    def dfs(self, startnode):

        startnode.visited = True
        print("%s " % startnode.data)

        for n in startnode.adjacencylist:
            if not n.visited:
                self.dfs(n)


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

dfsearch = Dfs()
dfsearch.dfs(node1)