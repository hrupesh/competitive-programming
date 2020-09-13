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

    def insert_values(self, list):
        self.head = None
        for i in list:
            self.insert_at_end(i)

    def insert_at(self, index, data):

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            count += 1
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        ll = ''

        while itr:
            ll += str(itr.data)+' ' if itr.next else str(itr.data)
            itr = itr.next

        print(ll)


if __name__ == "__main__":
    L = LinkedList()

    n = int(input())

    elems = []

    for i in range(n):
        t = int(input())
        elems.append(t)

    data = int(input())

    pos = int(input())

    L.insert_values(elems)
    L.insert_at(pos, data)
    L.print()
