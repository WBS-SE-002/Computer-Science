class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



my_stack = Stack()

my_stack.push(10)
my_stack.push(20)


print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())

print(my_stack.is_empty())
my_stack.pop()
print(my_stack.is_empty())

print(my_stack.size())