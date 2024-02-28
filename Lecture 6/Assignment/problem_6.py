class Node:
    """
        Lightweight, nonpublic class for storing a doubly linked node.
    """

    def __init__(self, element=None, prev=None, next=None):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference


class DoubleLinkedList:
    def __init__(self):
        """
            Create an empty DoubleLinkedList.
            You can also modify this function if needed
        """
        self._header = Node(None, None, None)
        self._trailer = Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
            Return the number of elements in the DoubleLinkedList.
        """
        return self._size

    def is_empty(self):
        """
            Return True if the DoubleLinkedList is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        result = "Header<-->"
        currNode = self._header._next
        while currNode is not self._trailer:
            result += str(currNode._element) + "<-->"
            currNode = currNode._next
        return result + "Trailer"

    def insertAtFirst(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def insert_after(self, node, predecessor):
        node._prev._next = node._next
        node._next._prev = node._prev

        predecessor._next._prev = node
        node._next = predecessor._next

        predecessor._next = node
        node._prev = predecessor
    def partition_list(self, pivot):
        # Please write your code here
        tmp = self._header._next

        # if tmp._element < pivot:
        #     less_tail = tmp
        #     tmp = tmp._next
        # else:
        #     less_tail = self._header

        less_tail = self._header

        while tmp != self._trailer and tmp._element != None:
            next_tmp = tmp._next
            if tmp._element < pivot:
                self.insert_after(tmp, less_tail)
                less_tail = tmp

            tmp = next_tmp

        # tmp = self._header._next
        # left_head = None
        # left_tail = None
        # right_head = None
        # right_tail = None
        #
        # while tmp != self._trailer:
        #     next_tmp = tmp._next
        #     if tmp._element < pivot:
        #         if left_head == None:
        #             left_head = tmp
        #             left_tail = tmp
        #         else:
        #             left_tail._next = tmp
        #             tmp._prev = left_tail
        #             left_tail = tmp
        #     elif tmp._element >= pivot:
        #         if right_head == None:
        #             right_head = tmp
        #             right_tail = tmp
        #         else:
        #             if tmp._element == pivot:
        #                 tmp._next = right_head
        #                 right_head._prev = tmp
        #                 right_head = tmp
        #             else:
        #                 right_tail._next = tmp
        #                 tmp._prev = right_tail
        #                 right_tail = tmp
        #     tmp = next_tmp
        #
        #
        # if left_tail != None and right_head != None:
        #     left_tail._next = right_head
        #     right_head._prev = left_tail
        #
        #     right_tail._next = self._trailer
        #     self._trailer._prev = right_tail
        #
        #     left_head._prev = self._header
        #     self._header._next = left_head
        #
        # elif left_tail == None:
        #     self._header._next = right_head
        #     right_head._prev = self._header
        #
        #     right_tail._next = self._trailer
        #     self._trailer._prev = right_tail
        #
        # elif right_head == None:
        #     self._header._next = left_head
        #     left_head._prev = self._header
        #
        #     left_tail._next = self._trailer
        #     self._trailer._prev = left_tail


def main():
    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(8)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(7)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(4)

    print(ls1)  # Should print: Header<-->5<-->1<-->6<-->2<-->7<-->3<-->8<-->4<-->Trailer
    ls1.partition_list(5)
    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->4<-->5<-->6<-->7<-->8<-->Trailer

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(8)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(7)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Header<-->5<-->1<-->6<-->2<-->7<-->3<-->8<-->4<-->Trailer
    ls1.partition_list(7)
    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->5<-->6<-->7<-->8<-->4<-->Trailer

if __name__ == '__main__':
    main()