##栈具有 后进先出特点


##模拟栈

class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def push(self,item):
        return self.items.append(item)
    def pop(self)
        return self.item.pop()
    def peek(self):
        if not self.isEmpty():
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


s=stack()
