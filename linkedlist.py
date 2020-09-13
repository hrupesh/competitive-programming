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

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        ll = ''

        while itr:
            if not itr.next:
                ll += str(itr.data)
            ll += str(itr.data) + '-->'
            itr = itr.next

        print(ll)
        
if __name__ == "__main__":
    L = LinkedList()
    L.insert_at_begining(1)
    L.insert_at_begining(2)
    L.insert_at_begining(3)
    L.insert_at_begining(4)
    L.print()