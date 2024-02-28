class Solution:
    def same(self, i1, i2):
        if len(i1) != len(i2):
            return False

        return self._same(i1, i2, len(i1))

    def _same(self, i1, i2, n):
        # if no element is present in the list, return true
        if n == 0:
            return True

        # if the first element differs in both lists (root node key), return false
        if i1[0] != i2[0]:
            return False

        # if the list contains only one key, return true
        if n == 1:
            return True

        # take four auxiliary spaces of size `n-1` each (as maximum keys in left or right subtree can be `n-1`)
        left_i1 = [None] * (n - 1)
        right_i1 = [None] * (n - 1)
        left_i2 = [None] * (n - 1)
        right_i2 = [None] * (n - 1)

        k = l = m = o = 0

        # process the remaining keys and divide them into two groups
        for i in range(1, n):

            # `left_i1` will contain all elements less than `X[0]`
            if i1[i] < i1[0]:
                left_i1[k] = i1[i]
                k = k + 1

            # `right_i1` will contain all elements more than `X[0]`
            else:
                right_i1[l] = i1[i]
                l = l + 1

            # `left_i2` will contain all elements less than `Y[0]`
            if i2[i] < i2[0]:
                left_i2[m] = i2[i]
                m = m + 1

            # `right_i2` will contain all elements more than `Y[0]`
            else:
                right_i2[o] = i2[i]
                o = o + 1

        # return false if the size of `left_i1` and `left_i2` differs, i.e.,
        # the total number of nodes in the left subtree of both trees differs
        if k != m:
            return False

        # return false if the size of `right_i1` and `right_i2` differs, i.e.,
        # the total number of nodes in the right subtree of both trees differs
        if l != o:
            return False

        # check left and right subtree
        return self._same(left_i1, left_i2, k) and self._same(right_i1, right_i2, l)


def main():
    i1 = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
    i2 = [15, 10, 12, 8, 25, 30, 6, 20, 18, 9, 22]

    res = Solution().same(i1, i2)
    print(res)  # Should print true


if __name__ == '__main__':
    main()
