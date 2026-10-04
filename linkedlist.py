class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    
    def __init__(self):
        self.top = None 
        self.count = 0
    
    def push(self, item):

        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):

        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data
    
    def peek(self):

        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):

        return self.top is None
    
    def size(self):

        return self.count

'''
if __name__ == "__main__":
    stack = LinkedListStack()
    

    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Top item:", stack.peek())
    print("Size:", stack.size())
    
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Is empty?", stack.is_empty())
    print("Popped:", stack.pop())
    print("Is empty?", stack.is_empty())
    '''