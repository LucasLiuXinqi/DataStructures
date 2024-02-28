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
        while currNode is not None and currNode._element[0] != target:
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

    def find_node(self, target):
        currNode = self._data._head
        while currNode is not None and currNode._element[0] != target:
            currNode = currNode._next
        return currNode

    def insertAtLast(self, e):
        newNode = Node(e, None)
        tail = self.get_tail()
        tail._next = newNode
        self._data._size += 1

    def get_tail(self):
        tmp = self._data._head

        while tmp._next != None:
            tmp = tmp._next

        return tmp
    def access(self, e):
        # Please write your code here
        if self._data.unOrderedSearch(e):
            node = self.find_node(e)
            node._element[1] += 1

            # if self._data._head == node:
            #     pass
            # else:
            #     prev_node = self._data.find_prev(node)
            #     prev_node._next = node._next
            #     node._next = self._data._head
            #     self._data._head = node


            # current = self._data._head
            # if current == node:
            #     pass
            # else:
            #     if self._data._size > 2:
            #         while current != None and current._next != node:
            #             if current._next._next != node:
            #                 current = current._next
            #             else:
            #                 break
            #
            #         if current._next != node:
            #             prev_node = current._next
            #             prev_prev_node = current
            #             prev_node._next = node._next
            #             prev_prev_node._next = node
            #             node._next = prev_node
            #
            #         else:
            #             if current == self._data._head:
            #                 current._next = node._next
            #                 node._next = current
            #                 self._data._head = node
            #
            #
            #     else:
            #         node._next = current
            #         self._data._head = node
            #         current._next = None

        else:
            if self._data.is_empty():
                self._data.insertAtFirst([e, 1])
            else:
                self.insertAtLast([e, 1])


    def __str__(self):
        return str(self._data)


def main():
    d = FavSinglyLinkedList()
    # for i in range(10):
    #     d.access('www.a')
    #     if i % 2 == 0:
    #         d.access('www.b')
    #     if i % 3 == 0:
    #         d.access('www.c')
    #     if i % 5 == 0:
    #         d.access('www.d')
    d.access('www.e')
    d.access('www.d')
    d.access('www.c')
    d.access('www.b')
    d.access('www.a')
    print(d)  # Expect "Head-->['www.a', 10]-->['www.b', 5]-->['www.c', 4]-->['www.d', 2]-->None"


if __name__ == '__main__':
    main()
