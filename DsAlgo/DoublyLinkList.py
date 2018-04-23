class node():
    def __init__(self, data):
        self.data = data
        self.nextnode = None
        self.prevnode = None

class DoublyLinkedList():

    def __init__(self):
        self.first = None
        self.size = 0

    def insert_val(self, data):

        newnode = node(data)
        self.size += 1

        if self.first is None:
            self.first = node(data)
        else:
            newnode.nextnode = self.first
            self.first.prevnode = newnode
            self.first = newnode

    def print_list_forward(self):
        iternode = self.first
        while iternode != None:
            print(iternode.data)
            iternode = iternode.nextnode

    def reverse(self, item):
        newitem = item
        if newitem.nextnode == None:
            iterit = newitem
            self._iterrev(iterit)
        else:
            self.reverse(newitem.nextnode)

    def _iterrev(self, iteritem):
       if iteritem.prevnode != None:
           print(iteritem.data)
           self._iterrev(iteritem.prevnode)
       else:
           print(iteritem.data)


doublylist = DoublyLinkedList()

doublylist.insert_val(10)
doublylist.insert_val(20)
doublylist.insert_val(30)
doublylist.insert_val(40)
doublylist.insert_val(50)

doublylist.print_list_forward()
print("----reverse-----")
doublylist.reverse(doublylist.first)

print(doublylist.size)