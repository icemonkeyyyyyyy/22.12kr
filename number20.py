class NaturalNumber:
    def __init__(self, value):
        self.value = value

    # оператор ==
    def sum_digit(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))

    def __eq__(self, other):
        if isinstance(other, NaturalNumber):
            return self.digit_sum(self.value) == other.digit_sum(other.value)
        elif isinstance(other, int):
            return self.digit_sum(self.value) == self.digit_sum(other)
        else:
            return False

    # оператор <
    def __lt__(self, other):
        if isinstance(other, NaturalNumber):
            return self.digit_sum(self.value) < other.digit_sum(other.value)
        elif isinstance(other, int):
            return self.digit_sum(self.value) < self.digit_sum(other)
        else:
            return False

    # оператор <=
    def __le__(self, other):
        if isinstance(other, NaturalNumber):
            return self.digit_sum(self.value) <= other.digit_sum(other.value)
        elif isinstance(other, int):
            return self.digit_sum(self.value) <= self.digit_sum(other)
        else:
            return False

    def __repr__(self):
        return str(self.value)


# n1 = NaturalNumber(189)
# n2 = NaturalNumber(456)
# n3 = NaturalNumber(789)
# n4 = NaturalNumber(198)
#
# print(n1 > n2)
# print(n1 < n3)
# print(n2 == n4)
