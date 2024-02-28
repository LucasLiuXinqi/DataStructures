class Node:
    def __init__(self, element=None, next=None):
        self._element = element
        self._next = next


class SingleLinkedList:
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

    def swapWithKth(self, k):
        """
            This function swaps the linked lists k-th and first node

            Throw Exception("Short") if the LinkedList is too short for the operation.
        """

        # Please write your code here
        pass
        if self._size < k:
            raise Exception("Short")

        tmp = self._head
        for i in range(k-2):
            tmp = tmp._next

        if k == 1:
            pass

        elif k == 2:
            node = self._head._next
            self._head._next = node._next
            node._next = self._head
            self._head = node

        elif k == self._size:
            node = tmp._next
            node._next = self._head._next
            tmp._next = self._head
            self._head._next = None
            self._head = node

        else:
            prev_node = tmp
            node = tmp._next
            next_node = node._next

            prev_node._next = self._head
            node._next = self._head._next
            self._head._next = next_node
            self._head = node



def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Head-->35-->22-->10-->5-->None
    ls1.swapWithKth(4)
    print(ls1)  # Should print: Head-->22-->35-->10-->5-->None

if __name__ == '__main__':
    main()
