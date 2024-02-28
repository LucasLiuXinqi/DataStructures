def max_word_count(filename):
    """
  # TODO: Use python dictionary to find the most frequent word in the input file
  # Please do not use the sorted(.) function for this exercise
  """
    max_word, max_count = '', 0

    # Phase 1: Count word occurrence
    dic = {}
    with open(filename, "r") as F:
        for line in F:
            words = line.strip().lower().split()
            for word in words:
                dic[word] = dic.get(word, 0) + 1
                if dic[word] > max_count:
                    max_word, max_count = word, dic[word]


    # Phase 2: Search a word with maximum occurrence
    # TODO: Use def items() in python dictionary to obtain a sequence of (key,value) pairs

    return max_word, max_count


if __name__ == '__main__':
    filename = 'inputtext2.txt'

    max_word, max_count = max_word_count(filename)

    print('The most frequent word is', max_word)  # Expect: interest
    print('Its number of occurrences is', max_count)  # Expect: 7