class Queue():

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        val = self.queue[0]
        del self.queue[0]
        return val

    def peek(self):
        val = self.queue[0]
        return val

    def getsize(self):
        return len(self.queue)


que = Queue()

que.enqueue(4)
que.enqueue(5)
que.enqueue(6)

print(que.peek())
print(que.dequeue())
print(que.peek())