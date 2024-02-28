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
        return newNode



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
        return newNode

    def get_tail(self):
        tmp = self._data._head

        while tmp._next != None:
            tmp = tmp._next

        return tmp

    def get_prev(self, node):
        # Check if the given node is the head of the list
        if node == self._data._head:
            return None  # There is no previous node
        else:
            # Search for the previous node
            current = self._data._head
            while current is not None and current._next != node:
                current = current._next

            if current is not None:
                return current
            else:
                raise ValueError("Node not found in the list")

    def swap_node(self, node1, node2):
        # Swap the positions of node1 and node2
        if node1 is None or node2 is None or node1 == node2:
            return

        prev1 = self.get_prev(node1)
        prev2 = self.get_prev(node2)

        if prev1:
            prev1._next = node2
        else:
            self._data._head = node2

        if prev2:
            prev2._next = node1
        else:
            self._data._head = node1

        tmp1 = node1._next
        tmp2 = node2._next

        node1._next, node2._next = tmp2, tmp1


    def access(self, e):
        # Please write your code here
        if self._data.unOrderedSearch(e):
            node = self.find_node(e)
            node._element[1] += 1

        else:
            if self._data.is_empty():
                node = self._data.insertAtFirst([e, 1])
            else:
                node = self.insertAtLast([e, 1])

        # tmp = self._data._head
        #
        # while tmp._next != None and tmp._element[1] > node._element[1]:
        #     if tmp._next._element[1] > node._element[1]:
        #         tmp = tmp._next
        #     else:
        #         break
        #
        # if tmp != self._data._head:
        #     prev_node = self.get_prev(node)
        #     prev_node._next = node._next
        #     node._next = tmp._next
        #     tmp._next = node
        #
        # else:
        #     prev_node = self.get_prev(node)
        #     if node._next:
        #         prev_node._next = node._next
        #     else:
        #         prev_node._next = None
        #     node._next = tmp
        #     self._data._head = node


        prev_node = self.get_prev(node)
        while prev_node and prev_node._element[1] <= node._element[1]:
            prev_node = self.get_prev(node)
            self.swap_node(prev_node, node)

        print(self._data)

    def leastk(self, k):
        # Please write your code here
        stack = []
        node = self._data._head
        while node != None:
            stack.append(node)
            node = node._next

        for i in range(k):
            if stack:
                url = stack.pop()._element[0]
                yield url

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
    # d.access('www.e')
    # d.access('www.d')
    # d.access('www.c')
    # d.access('www.b')
    # d.access('www.a')
    print(d)  # Expect "Head-->['www.a', 10]-->['www.b', 5]-->['www.c', 4]-->['www.d', 2]-->None"

    for each in d.leastk(3):
        print(each)


if __name__ == '__main__':
    main()
