from typing import List
from math import acos, pi


# Common Words
def checkio_common_words(first, second):
    return ','.join(sorted([x for x in first.split(',') for y in second.split(',') if x == y]))


# The Angles of Triangle
def checkio(a: int, b: int, c: int) -> List[int]:
    if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
        alfa = round(acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c)) * 180 / pi)
        beta = round(acos((a ** 2 + c ** 2 - b ** 2)/(2 * a * c)) * 180 / pi)
        gamma = 180 - alfa - beta
        return sorted([alfa, beta, gamma])
    return [0, 0, 0]

if __name__ == '__main__':
    assert checkio_common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio_common_words("one,two,three", "four,five,six") == "", "Too different"
    assert checkio_common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"