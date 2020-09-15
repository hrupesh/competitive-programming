#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def getNode(head, positionFromTail):
    llist = SinglyLinkedList()
    llist.head = head

    count = 0
    itr = llist.head
    while itr:
        count += 1
        itr = itr.next

    index = count - positionFromTail
    itr1 = llist.head
    count1 = 0
    data = 0
    while itr1:
        if  count1 == index:
            data = itr1.data
        count1 += 1
        itr1 = itr1.next

    return data

if __name__ == '__main__':