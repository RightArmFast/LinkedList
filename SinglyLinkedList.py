# simple Linked List class with basic CRUD operations
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append(self, value):
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
        print("\n")

    def delete_at_index(self, index):
        if (self.head == None):
            print("There are no nodes to delete!")
            return

        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return

        # get to the node right before the one we want to delete
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None or temp.next is None:
            print("Specified index is longer than the list!")
            return

        # have a temporary node pointing to node after the one we want to delete
        next = temp.next.next
        temp.next = None
        temp.next = next

    #delete the first occurence of a value
    def delete(self, value):
        if self.head == None:
            print("No nodes to delete!")
            return

        #if the node we are deleting is at the first position
        if self.head.value == value:
            temp = self.head
            next = temp.next
            self.head = next
            return

        current = self.head
        previous = None
        while current is not None and current.value != value:
            previous = current
            current = current.next

        if current is None:
            print("Value was not found in the list!")
            return

        previous.next = current.next
        current.next = None


    def search(self, key):
        current = self.head
        index = 0
        while current != None and current.value != key:
            current = current.next
            index += 1

        if current == None:
            print("Key was not found in the linked list!")
        else:
            print(f"Key found at position {index}! Returning node")
            return current


