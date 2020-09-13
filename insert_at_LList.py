class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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
        if index < 0 or index >= self.length():
        raise Exception(f'Invalid index {index}')

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


if __name__ == "__main__":
    L = LinkedList()

    n = int(input())

    elems = []

    for i in range(n):
        t = input()
        elems.append(t)

    data = input()

    pos = input()

    L.insert_multiple(elems)
    L.insert_at(pos, data)
    L.print()
