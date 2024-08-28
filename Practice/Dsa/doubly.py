class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly:
    def __init__(self):
        self.head = None

    def insertatbegin(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head.prev = newnode
            newnode.next = self.head
        self.head = newnode
    
    def insertatend(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newnode
            newnode.prev = last

    def insertatindex(self,data,index):       
        newnode = Node(data)
        if self.head is None:
            return
        if self.head == index:
            self.head = newnode
        else:
            current = self.head
            position = 0
            while current.next and position 



