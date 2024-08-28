class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the head of the list
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    # Insert at the tail of the list
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Insert after a specific node
    # def insert_after(self, prev_node, data):
    #     if prev_node is None:
    #         print("The given previous node cannot be None")
    #         return
    #     new_node = Node(data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node
    #     new_node.prev = prev_node
    #     if new_node.next is not None:
    #         new_node.next.prev = new_node

                # -------------
    

    # def insert_at_index(self, index, data):
    #     if index < 0:
    #         print("Index cannot be negative")
    #         return

    #     new_node = Node(data)

    #     if self.head is None:
    #         if index == 0:
    #             self.head = new_node
    #         else:
    #             print("Index out of bounds")
    #         return

    #     if index == 0:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node
    #         return

    #     current = self.head
    #     count = 0

    #     while current is not None and count < index - 1:
    #         current = current.next
    #         count += 1

    #     if current is None:
    #         print("Index out of bounds")
    #         return

    #     new_node.next = current.next
    #     new_node.prev = current
    #     if current.next is not None:
    #         current.next.prev = new_node
    #     current.next = new_node


    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


    # Delete a node from the head of the list
    def delete_from_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    # Delete a node from the tail of the list
    def delete_from_tail(self):
        if self.head is None:
            return
        last = self.head
        if last.next is None:
            self.head = None
            return
        while last.next is not None:
            last = last.next
        last.prev.next = None

    # Delete a specific node
    def delete_node(self, node):
        if self.head is None or node is None:
            return
        if node == self.head:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

    # Print the list
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_tail(20)
    dll.insert_at_tail(30)
    dll.insert_at_head(5)
    dll.print_list()  # Output: 5 10 20 30
    dll.delete_from_head()
    dll.print_list()  # Output: 10 20 30
    dll.delete_from_tail()
    dll.print_list()  # Output: 10 20
    dll.insert_after(dll.head, 15)
    dll.print_list()  # Output: 10 15 20
    dll.delete_node(dll.head.next)
    dll.print_list()  # Output: 10 20
