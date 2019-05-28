# node class
class Node:
    def __init__(self, data):
        self.data = data  # assign a data
        self.next = None  # initialize


class LinkedList:
    def __init__(self):
        self.head = None

    # Linked List Traversal
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # add a node at the front
    # time complexity O(1)
    def push_bg(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # add a node in the middle
    # time complexity O(1)
    def insert_mid(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in the LL")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # add a node at end
    # time complexity O(n)
    def append(self, new_data):
        new_node = Node(new_data)
        # if the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    # remove the nodes
    def remove(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    # reversal the linked list
    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push_bg(7)
    llist.push_bg(1)
    llist.insert_mid(llist.head, 8)
    llist.insert_mid(llist.head, 5)
    llist.append(3)
    llist.remove(1)
    llist.remove(5)
    llist.printList()  # 8 7 6 3
