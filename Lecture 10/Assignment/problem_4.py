class Solution:
    def same(self, i_1, i_2):

        if len(i_1) != len(i_2):
            return False

        if len(i_1) == len(i_2) and len(i_1) == 0:
            return True
        elif len(i_1) == len(i_2) and len(i_1) == 1:
            return i_1 == i_2

        root_1 = i_1[0]
        left_1 = [i for i in i_1[1:] if i < root_1]
        right_1 = [i for i in i_1[1:] if i > root_1]

        root_2 = i_2[0]
        left_2 = [i for i in i_2[1:] if i < root_2]
        right_2 = [i for i in i_2[1:] if i > root_2]

        if root_1 == root_2 and self.same(left_1, left_2) and self.same(right_1, right_2):
            return True
        else:
            return False






def main():
    # i1 = [15, 25, 20, 22, 30, 18, 10, 8, 9, 12, 6]
    # i2 = [15, 10, 12, 8, 25, 30, 6, 20, 18, 9, 22]



    res = Solution().same(i1, i2)
    print(res)  # Should print true


if __name__ == '__main__':
    main()
