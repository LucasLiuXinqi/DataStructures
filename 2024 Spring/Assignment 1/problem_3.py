class Fraction:
    """
       This class provides arithmetic functions for handling fractions.
       Implement the given methods as described in the worksheet.
    """

    # Please write your code here
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
        if self.denominator == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        if self.denominator == other.denominator:
            output = Fraction(self.numerator, self.denominator)
            output.numerator += other.numerator
            return output

        else:
            output = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
            return output

    def __iadd__(self, other):
        if self.denominator == other.denominator:
            self.numerator += other.numerator
            return self
        else:
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
            return self

    def __sub__(self, other):
        if self.denominator == other.denominator:
            output = Fraction(self.numerator, self.denominator)
            output.numerator -= other.numerator
            return output

        else:
            output = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
            return output

    def __mul__(self, other):
        output = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return output

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __truediv__(self, other):
        output = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return output

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


def main():
    f1 = Fraction(2, 5)
    f2 = Fraction(2, 5)
    f3 = Fraction(3, 6)

    res = f3 / (f1-f2)
    print(res)

    # res = f1 + f2  # should print "3/5"
    # print(res)
    #
    # res = f1 - f2  # should print "-1/5"
    # print(res)
    #
    # res = f1 * f2  # should print "2/25"
    # print(res)
    #
    # res = f1 + f3  # should print "7/10"
    # print(res)
    #
    # res = f1 / f2  # should print "1/2"
    # print(res)


if __name__ == '__main__':
    main()
