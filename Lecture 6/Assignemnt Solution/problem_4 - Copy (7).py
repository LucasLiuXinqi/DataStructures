class Node:
    def __init__(self, element=None, next=None):
        self._element = element
        self._next = next


class SinglyLinkedList:
    def __init__(self):
        """Create an empty LinkedList."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the LinkedList."""
        return self._size

    def is_empty(self):
        """Return True if the LinkedList is empty."""
        return self._size == 0

    def insertAtFirst(self, e):
        """Add element e to the start of the LinkedList."""
        newNode = Node(e, self._head)
        self._head = newNode
        self._size += 1

    def insertLast(self, e):
        """Add element e to the last of the LinkedList."""
        if self._head is None:
            self._head = Node(e, None)
        else:
            cur = self._head
            while cur._next is not None:
                cur = cur._next
            cur._next = Node(e, None)

    def deleteFirst(self):
        """Remove and return the first element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the first node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        """Remove and return the last element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the last node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode._element) + "-->"
            currNode = currNode._next
        return result + "None"


class FavSinglyLinkedList:
    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        # Please write your code here
        _node = self.find(e)
        if _node:
            _node._element[1] += 1
        else:
            self._data.insertLast([e, 1])

    def find(self, e):
        currNode = self._data._head
        while currNode is not None and currNode._element[0] != e:
            currNode = currNode._next
        return currNode

    def leastk(self, k):
        # Please write your code here
        output = []
        for i in range(k):
            least = None
            currNode = self._data._head
            while currNode:
                if least is None or currNode._element[1] < least:
                    if currNode._element not in output:
                        _node = currNode
                        least = currNode._element[1]
                currNode = currNode._next

            yield _node._element[0]
            output.append(_node._element)

    def __str__(self):
        return str(self._data)


def main():
    d = FavSinglyLinkedList()
    for i in range(10):
        d.access('www.a')
        if i % 2 == 0:
            d.access('www.b')
        if i % 3 == 0:
            d.access('www.c')
        if i % 5 == 0:
            d.access('www.d')
    print(d)  # Expect "Head-->['www.a', 10]-->['www.b', 5]-->['www.c', 4]-->['www.d', 2]-->None"

    for each in d.leastk(3):
        print(each)
        # Expect 'www.d'
        #        'www.c'
        #        'www.b'
        #  in this order


if __name__ == '__main__':
    main()
