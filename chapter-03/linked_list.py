class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
       def __init__(self):
           self.head = None 
           self.tail = None
           self.length = 0

       def push(self, value):
        node = Node(value)
        self.length += 1
        if not self.head:
            self.head = node
        else: 
            self.tail.next = node
        self.tail = node

       def addFirst(self, value):
           newNode = Node(value)
           newNode.next = self.head
           self.head = newNode
           self.length += 1

       def _find(self, index):
           if index >= self.length:
               return None
           current = self.head
           for i in range(index):
               current = current.next
            
           return current

       def insertAt(self, index, value):
           if index == self.length -1:
               self.push(value)
           elif index == 0:
               self.addFirst(value)
           else:
               newNode = Node(value)
               node = self._find(index-1)
               newNode.next = node.next
               node.next = newNode


       def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

       def delete(self, index):
            if index == 0:
                head = self.head
                if head:
                    self.head = head.next
                else:
                    self.head = None
                    self.tail = None
                
                self.length -= 1
                return head.value

            
            node = self._find(index -1)
            excise = node.next;
            if not excise:
                return None
            node.next = excise.next
            if not node.next:
                self.tail = node
            self.length -= 1
            return excise.value
            


        



def reverse_linkedlist(list):
    start = list.head
    list.head = list.tail
    list.tail = start
    reverse_pointer(start)

def reverse_pointer(node):
    if node.next == None:
        return
    reverse_pointer(node.next)
    node.next.next = node
    node.next = None







# pre recursion
# recursion
# post recursion


# def _reverse(self, current_head):
#         if current_head is None or current_head.next is None:
#             return current_head

#         rest_head = self._reverse(current_head.next)

#         current_head.next.next = current_head
#         current_head.next = None

#         return rest_head

# def reverse(self):
#         self.head = self._reverse(self.head)



# def reverse1(self):
#     prev = None
#     current = self.head

#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node

#     self.head = prev