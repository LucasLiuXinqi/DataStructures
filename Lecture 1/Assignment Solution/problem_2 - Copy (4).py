class IterableIterator:
    def __init__(self):
        self._count = 1

    def __len__(self):
        return 20

    def __getitem__(self, index):
        return (index % 20) + 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self._count
        self._count = (self._count % 20) + 1
        return value


def main():
    my_obj = IterableIterator()
    my_it = iter(my_obj)
    print(my_obj[41])  # Output: 2
    print(next(my_it), next(my_it), next(my_it), next(my_it))  # Output: 1 2 3 4


if __name__ == '__main__':
    main()
