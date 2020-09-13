class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        ll = ''

        while itr:
            ll += str(itr.data)+'-->' if itr.next else str(itr.data)
            # ll += itr.next ? str(itr.data) + '-->': str(itr.data)
            itr = itr.next

        print(ll)


if __name__ == "__main__":
    L = LinkedList()
    L.insert_at_begining(2)
    L.insert_at_begining(1)
    L.insert_at_end(3)
    L.insert_at_end(4)
    L.print()
