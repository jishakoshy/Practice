class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head =None

    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
            return self.head
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    
    def is_prime(self,num):
        if num <= 1:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

    def check_isprim(self):
        current = self.head
        while self.head is not None:
            if self.is_prime(current.data):
                print(current.data ,"is prime")
            else:
                print(current.data,"is not prime")
            current = current.next
