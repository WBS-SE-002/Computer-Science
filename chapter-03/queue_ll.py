from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.items = LinkedList()


    def enqueue(self, item):
        self.items.push(item)

    def dequeue(self):
        self.items.delete(0)

    def peek(self):
        return self.items.head

    def size(self):
        return self.items.length


    def isEmpty(self):
        return self.items.length == 0

    def printQueue(self):
        self.items.printList()


myQueue = Queue()


myQueue.enqueue("A")
myQueue.enqueue("B")

myQueue.printQueue()


