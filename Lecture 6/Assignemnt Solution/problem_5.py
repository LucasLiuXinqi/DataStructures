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
        self._insert_between(e, self._header, self._header._next)

    def shuffle(self):
        # Please write your code here
        target, base, successor = self._trailer._prev, self._header._next, self._header._next._next
        for _ in range(len(self) // 2 - 1):
            next_target = target._prev
            self.remove_and_insert(target, base, successor)
            target, base, successor = next_target, successor, successor._next
        return self

    def remove_and_insert(self, target, predecessor, successor):
        target._prev._next = target._next
        target._next._prev = target._prev
        target._prev, target._next = predecessor, successor
        predecessor._next = target
        successor._prev = target
        return self


def main():
    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)

    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->4<-->Trailer
    ls1.shuffle()
    print(ls1)  # Should print: Header<-->1<-->4<-->2<-->3<-->Trailer


if __name__ == '__main__':
    main()
