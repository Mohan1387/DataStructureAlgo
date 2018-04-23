class node():
    def __init__(self, data):
        self.data = data
        self.nextnode = None


class Linkedlist(object):

    def __init__(self):
        self.first = None
        self.size = 0

    def insert_val(self, data):
        newnode = node(data)
        self.size += 1
        if self.first == None:
            self.first = newnode
        else:
            newnode.nextnode = self.first
            self.first = newnode

    def getSize(self):
        return self.size

    def print_list(self):
        iternode = self.first
        while iternode != None:
            print(iternode.data)
            iternode = iternode.nextnode

    def find_next(self, val):
        iternode = self.first
        while iternode != None:
            if iternode.data == val:
                return iternode.nextnode.data
            iternode = iternode.nextnode

    def remove_val(self, val):

        if self.first is None:
            return

        curnode = self.first
        prenode = None

        self.size -= 1
        while curnode.data != val:
            prenode = curnode
            curnode = curnode.nextnode

        if prenode is None:
            self.first = curnode.nextnode
        else:
            prenode.nextnode = curnode.nextnode




linklist = Linkedlist()
linklist.insert_val(10)
linklist.insert_val(20)
linklist.insert_val(30)
linklist.insert_val(40)
linklist.insert_val(50)

print(linklist.getSize())

#find next node value of given value
print(linklist.find_next(40))

#print list
linklist.print_list()

#remove _node
linklist.remove_val(30)

#print list
linklist.print_list()

print(linklist.getSize())