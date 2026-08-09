class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next

ssl = SingleLinkedList()
ssl.append(10)
ssl.append(9)
ssl.append(22)
ssl.append(23)
ssl.traverse()
