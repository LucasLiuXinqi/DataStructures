
def string_generator():
    # Please write your code here
    pass
    word_list = list('catdog')
    for i in range(6):
        letter_1 = word_list[i]
        sub_1 = word_list[:i] + word_list[i+1:]

        for j in range(5):
            letter_2 = sub_1[j]
            sub_2 = sub_1[:j] + sub_1[j+1:]

            for k in range(4):
                letter_3 = sub_2[k]
                sub_3 = sub_2[:k] + sub_2[k+1:]

                for l in range(3):
                    letter_4 = sub_3[l]
                    sub_4 = sub_3[:l] + sub_3[l+1:]

                    for m in range(2):
                        letter_5 = sub_4[m]
                        sub_5 = sub_4[:m] + sub_4[m+1:]
                        letter_6 = sub_5[0]
                        yield letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + letter_6

def main():
    cat_dog = string_generator()

    print(next(cat_dog))  # Output: "catdgo" or another combination
    print(next(cat_dog))  # Output: "catdgo" or another combination
    print(next(cat_dog))  # Output: "catodg" or another combination


if __name__ == '__main__':
    main()

