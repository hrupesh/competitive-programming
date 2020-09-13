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

    def insert_multiple(self, list):
        for i in list:
            self.insert_at_end(i)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        ll = ''

        while itr:
            ll += str(itr.data)+'->' if itr.next else str(itr.data)
            itr = itr.next

        print(ll)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    L = LinkedList()
    L.insert_values([1, 2, 1, 1])
    L.insert_at_begining(1)
    L.insert_at_end(4)
    L.insert_multiple([3, 4, 5, 6])
    L.print()
    print(L.length())
    L.remove_at(0)
    L.remove_at(5)
    L.print()
    print(L.length())
