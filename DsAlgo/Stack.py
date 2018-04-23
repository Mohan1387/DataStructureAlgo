# Recursive function uses stack at the backend
# lets find the factorial of given number
#def fac(n):
#    if n == 0:
#        return 1
#    else:
#        return n * fac(n-1)
#print(fac(4))

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def peek(self):
        val = self.stack[-1]
        return val

    def getsize(self):
        return len(self.stack)


stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)

print(stk.peek())
print(stk.getsize())
print(stk.pop())
print(stk.getsize())
print(stk.peek())

