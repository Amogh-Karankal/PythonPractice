class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def inset_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


fam = LinkedList()
fam.head = Node("Bob")
wife = Node("Amy")
first_child = Node("Max")
sec_child = Node("Jenny")

fam.head.next = wife
wife.next = first_child
first_child.next = sec_child

fam.inset_new_header("Dave")
fam.traversal()
fam.delete_node("Bob")
fam.traversal()
fam.delete_tail()
fam.traversal()
print(fam.search("Bob"))