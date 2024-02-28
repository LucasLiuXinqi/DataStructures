class IterableIterator:
    # Please write your code here
    def __init__(self):
        self.current = 0
        self.number = [i for i in range(1, 21)]

    def __next__(self):
        if self.current <= 19:
            value = self.number[self.current]
            self.current += 1
            return value
        else:
            self.current = 0
            return self.number[0]

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.number)

    def __getitem__(self, n):
        return self.number[n % 20]



def main():
    my_obj = IterableIterator()
    my_it = iter(my_obj)
    print(my_obj[41])  # Output: 2
    print(next(my_it), next(my_it), next(my_it), next(my_it))  # Output: 1 2 3 4


if __name__ == '__main__':
    main()

