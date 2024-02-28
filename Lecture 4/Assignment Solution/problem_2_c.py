import ctypes


class UserDefinedDynamicArray:
    def __init__(self, I=None):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self, x):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = x
        self._n += 1

    def _resize(self, newsize):
        A = self._make_array(newsize)
        self._capacity = newsize
        for i in range(self._n):
            A[i] = self._A[i]
        self._A = A

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def __getitem__(self, i):
        if isinstance(i, slice):
            A = UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)):
                A.append(self._A[j])
            return A
        if i < 0:
            i = self._n + i
        return self._A[i]

    def __delitem__(self, i):
        if isinstance(i, slice):
            for j in reversed(range(*i.indices(self._n))):
                del self[j]
        else:
            if i < 0:
                i = self._n + i
            for j in range(i, self._n - 1):
                self._A[j] = self._A[j + 1]
            self[-1] = None
            self._n -= 1
            if self._n * 4 <= self._capacity:
                new_cap = self._n * 2
                self._resize(new_cap)

    def __str__(self):
        return "[" \
            + "".join(str(i) + "," for i in self[:-1]) \
            + (str(self[-1]) if not self.is_empty() else "") \
            + "]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        for i in range(self._n):
            yield self._A[i]

    def __setitem__(self, i, x):
        if i >= 0:
            self._A[i] = x
        else:
            self._A[self._n - abs(i)] = x

    def extend(self, I):
        for i in I: self.append(i)

    def reverse(self):
        l = self._n
        for i in range(l):
            if i * 2 >= l - 1: break
            k = self[i]
            self[i] = self[l - 1 - i]
            self[l - 1 - i] = k

    def __contains__(self, x):
        for i in range(self._n):
            if self._A[i] == x:
                return True
        return False

    def index(self, x):
        for i in range(self._n):
            if self._A[i] == x:
                return i
        return None

    def count(self, x):
        count = 0
        for i in range(self._n):
            if i == x:
                count += 1
        return count

    def __add__(self, other):
        pass
        l = []
        l.extend(self)
        l.extend(other)
        return l

    def __mul__(self, times):
        l = []
        for i in range(times):
            l.extend(self)
        return l

    __rmul__ = __mul__

    def pop(self, i=-1):
        del self[i]

    def remove(self, x):
        p = self.index(x)
        del self[p]

    def max(self):
        candidate = self._A[0]
        for i in range(self._n):
            if self._A[i] > candidate:
                candidate = self._A[i]
        return candidate

    def min(self):
        candidate = self._A[0]
        for i in range(self._n):
            if self._A[i] < candidate:
                candidate = self._A[i]
        return candidate

    def sort(self, order="asc"):
        l = []
        l = list(self)
        l.sort()
        if order == 'desc': l.reverse()
        self._A = UserDefinedDynamicArray(l)

    def union(self, b):
        """
           This function returns the union of lists l1 and l2
        """
        # Please write your code here
        res = UserDefinedDynamicArray()
        i, j = 0, 0
        while i < len(self) and j < len(b):
            if self[i] == b[j]:
                res.append(self[i])
                i += 1
                j += 1
            elif self[i] > b[j]:
                res.append(b[j])
                j += 1
            else:
                res.append(self[i])
                i += 1

        if i < len(self):
            res += self[i:]
        elif j < len(b):
            res += b[j:]

        return res

    def intersect(self, b):
        """
           This function returns the intersection of lists l1 and l2
        """
        # Please write your code here
        res = UserDefinedDynamicArray()
        i, j = 0, 0
        while i < len(self) and j < len(b):

            if self[i] == b[j]:
                res.append(self[i])
                i += 1
                j += 1
            elif self[i] > b[j]:
                j += 1
            else:
                i += 1

        return res


def main():
    L1 = UserDefinedDynamicArray([1, 3, 5, 7, 9])
    L1.sort()
    L2 = UserDefinedDynamicArray([3, 4, 5, 6, 7])
    L2.sort()
    L3 = UserDefinedDynamicArray([2, 4, 6, 8, 10])
    L3.sort()

    L = L1.union(L2)
    L.sort()  # L should be the same as UserDefinedDynamicArray([1,3,4,5,6,7,9])
    print(L)

    L = L2.intersect(L3)
    L.sort()  # L should be the same as UserDefinedDynamicArray([4,6])
    print(L)


if __name__ == '__main__':
    main()
