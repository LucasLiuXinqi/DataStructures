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

    def tailswap(self):
        """
            This function swaps the linked lists last and second last node

            Throw Exception("Short") if the LinkedList is too short for the operation.
        """

        # Please write your code here
        # Time complexity requirement: O(n)
        # Space complexity requirement: O(1)

        # throw exception if the list does not contain two nodes
        if self._size < 2:
            raise Exception("Short")

        if self._size == 2:
            temp = self._head._next
            self._head._next = self._head._next._next
            temp._next = self._head

            # assign head pointer
            self._head = temp
            return

        current_node = self._head
        # traverse to the end of the list
        for i in range(self._size - 3):
            current_node = current_node._next

        temp1 = current_node._next
        temp2 = temp1._next
        temp1._next = None
        temp2._next = temp1
        current_node._next = temp2


def main():
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Head-->35-->22-->10-->5-->None
    ls1.tailswap()
    print(ls1)  # Should print: Head-->35-->22-->5-->10-->None


if __name__ == '__main__':
    main()
