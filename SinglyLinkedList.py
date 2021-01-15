#simple Linked List class with insert, search, delete and print operations
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def delete(self, index):
        if(self.head == None):
            print("There are no nodes to delete!")

        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return

        currentIndex = 0
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break







        
    

LL = SinglyLinkedList()

LL.insert(5)
LL.insert(4)
LL.insert(3)

LL.print()

