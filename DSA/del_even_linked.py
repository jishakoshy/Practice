class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def is_even(self,num):
        return num % 2 == 0


    def check_even(self):
        current = self.head
        while self.head is not None:
            if self.is_even(self.current.data):
                print(current.data,"is even")
            else:
                print(current.data,"is not even")


