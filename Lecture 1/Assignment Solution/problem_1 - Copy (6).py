def string_generator():
    characters = 'catdog'
    n = len(characters)

    # Initialize a list of indices to keep track of the current permutation
    indices = list(range(n))

    while True:
        yield ''.join(characters[i] for i in indices)

        # Find the rightmost character that can be incremented
        j = n - 1
        while j > 0 and indices[j - 1] > indices[j]:
            j -= 1

        # If no such character is found, we've generated all permutations
        if j == 0:
            break

        # Find the smallest character to the right of j that is greater than indices[j-1]
        k = n - 1
        while indices[k] < indices[j - 1]:
            k -= 1

        # Swap characters at positions j-1 and k
        indices[j - 1], indices[k] = indices[k], indices[j - 1]

        # Reverse the suffix starting at position j
        indices[j:] = indices[j:][::-1]


def main():
    cat_dog = string_generator()
    print(next(cat_dog))  # Output: "catdog" or another combination
    print(next(cat_dog))  # Output: "catdgo" or another combination
    print(next(cat_dog))  # Output: "catodg" or another combination


if __name__ == '__main__':
    main()
