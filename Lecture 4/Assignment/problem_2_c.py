import ctypes


class UserDefinedDynamicArray:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A=UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __delitem__(self,i):  # Remove by index
        # >>> l = [1, 2, 3, 4] (Example)
        # >>> del l[0]
        # >>> del l[0]
        # >>> l
        # [3, 4]
        # Task 8
        # Current version __delitem__ does not shrink the array capacity.
        #
        # We want to shrink the array capacity by half if total number of
        # actual elements reduces to one fourth of the capacity.

        if isinstance(i,slice):
            #A=UserDefinedDynamicArray()
            for j in reversed(range(*i.indices(self._n))):
                 del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None        # Calls __setitem__
            self._n-=1
            # TODO
            # Missing some code for Task 8, shrink the size.
            if self._n <= self._capacity // 4:
                self._resize(self._capacity // 2)


    def __str__(self):
        return "[" \
               +"".join( str(i)+"," for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def is_empty(self):
        return self._n == 0

    def __iter__(self):
        # Task 1
        # iterate through the list using yield
        # Your Code
        for i in range(self._n):
            yield self._A[i]

    def __setitem__(self,i,x):
        # Task 2
        # think about how to handle negative index
        # Your code
        if i < 0:
          i = self._n + i

        self._A[i] = x


    def extend(self,I):
        # Task 3
        # append all elements of I to the self
        # Your code
        for i in I:
          self.append(i)

    def reverse(self):
        # Task 4
        # reverse the list
        # your code
        for i in range(self._n // 2):
          self._A[i], self._A[self._n - i - 1] = self._A[self._n - i - 1], self._A[i]

    def __contains__(self,x):
        # Task 5
        # If element x is present in the list return true otherwise false
        # your code

        for i in range(self._n):
          if self._A[i] == x:
            return True

        return False

    def index(self,x):
        # Task 5
        # Return the index of first occurrence of element x, if not found in the list return None.
        # Your code
        for i in range(self._n):
          if self._A[i] == x:
            return i

        return None

    def count(self,x):
        # Task 5
        # return how many times element x is present in the list
        # Your code
        count = 0
        for i in range(self._n):
          if self._A[i] == x:
            count += 1

        return count

    def __add__(self,other):
        # Task 6
        # '+' Operator Overloading for UserDefinedDyamicArray Class like myList1+myList2 will return a list containing all the elements of myList1 and then myList2
        # Your code
        self.extend(other)
        return self

    def __mul__(self,times):
        # Task 6
        # '*' Operator Overloading for UserDefinedDyamicArray Class like myList1*3 will return a list having myList1 elements three times.
        # Your code
        for i in range(times):
          self.extend(self._A)

        return self

    __rmul__=__mul__

    def pop(self,i=-1):
        # Task 7
        # delete element at position i using del keyword, by default we delete the last element from UserDefinedDyamicArray and return the element to the calling method
        # Your Code
        ele = self._A[i]
        del self[i]
        return ele

    def remove(self,x):     # Remove by value
        # Task 7
        # remove element x from the list, we will delete the first occurrence of element x from the list
        # at first find out the index of element x, then call __del__(self, i) to delete it
        # Your code
        for i in range(self._n):
          if self._A[i] == x:
            del self[i]
            break


    def max(self):
        # Task 9
        # Return the max element in self._A
        # Your code
        max = self._A[0]
        for i in range(self._n):
          if self._A[i] >= max:
            max = self._A[i]

        return max



    def min(self):
        # Task 9
        # Return the min element in self._A
        # Your code
        min = self._A[0]
        for i in range(self._n):
          if self._A[i] <= min:
            min = self._A[i]

        return min


    def sort(self, order = "asc"):
        # Task 10
        # Sort self._A in ascending order if order == "asc"
        # otherwise sort in descending order if order = 'desc'
        # if order parameter value is wrong, do nothing.
        # Your code
        if order == 'asc':
            for i in range(self._n):
                for j in range(i+1,self._n):
                    if self._A[i] > self._A[j]:
                        self._A[i],self._A[j] = self._A[j],self._A[i]

        elif order == 'desc':
            for i in range(self._n):
                for j in range(i+1,self._n):
                    if self._A[i] < self._A[j]:
                        self._A[i],self._A[j] = self._A[j],self._A[i]



    def union(self, b):
        # Please write your code here
        len_1 = self._n
        len_2 = b._n
        current_position = 0
        target_position = 0
        uni = []

        while current_position < len_1 and target_position < len_2:
            if self[current_position] < b[target_position]:
                uni.append(self[current_position])
                current_position += 1

            elif self[current_position] == b[target_position]:
                uni.append(self[current_position])
                current_position += 1
                target_position += 1

            elif self[current_position] > b[target_position]:
                uni.append(b[target_position])
                target_position += 1

        if current_position < len_1:
            uni += self[current_position:]

        if target_position < len_2:
            uni += b[target_position:]

        return uni

    def intersect(self, b):
        # Please write your code here
        len_1 = self._n
        len_2 = b._n
        current_position = 0
        target_position = 0
        intersection = []
        while current_position < len_1 and target_position < len_2:
            if self[current_position] < b[target_position]:
                current_position += 1

            elif self[current_position] == b[target_position]:
                intersection.append(self[current_position])
                current_position += 1
                target_position += 1

            elif self[current_position] > b[target_position]:
                target_position += 1

        return intersection


def main():
    L1 = UserDefinedDynamicArray([1, 3, 5, 7, 9])
    L1.sort()
    L2 = UserDefinedDynamicArray([3, 4, 5, 6, 7])
    L2.sort()
    L3 = UserDefinedDynamicArray([2, 4, 6, 8, 10])
    L3.sort()

    L = L1.union(L2)
    L.sort()  # L should be the same as UserDefinedDynamicArray([1, 3, 4, 5, 6, 7, 9])
    print(L)

    L = L2.intersect(L3)
    L.sort()  # L should be the same as UserDefinedDynamicArray([4, 6])
    print(L)


if __name__ == '__main__':
    main()
