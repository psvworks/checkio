from typing import List
from math import acos, pi, log


# Common Words
def checkio_common_words(first, second):
    return ','.join(sorted([x for x in first.split(',') for y in second.split(',') if x == y]))


# The Angles of Triangle
def checkio(a: int, b: int, c: int) -> List[int]:
    if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
        alfa = round(acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c)) * 180 / pi)
        beta = round(acos((a ** 2 + c ** 2 - b ** 2)/(2 * a * c)) * 180 / pi)
        gamma = 180 - (alfa + beta)
        return sorted([alfa, beta, gamma])
    return [0, 0, 0]


# Friendly Number
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    power = 0
    if number != 0:
        power = round(log(abs(number), base) // 1)
    if power > len(powers) - 1:
        power = len(powers) - 1
    sign = ''
    if number < 0:
        sign = '-'
    if abs(number) > base:
        if decimals == 0:
            result = str(abs(number) // (base ** power))
            return sign + result + powers[power] + suffix
        else:
            result = str(round(abs(number) / (base ** power), decimals))
            return sign + (result[::-1].zfill(decimals + len(result) - 1))[::-1] + powers[power] + suffix
    else:
        if decimals == 0:
            return str(round(number, decimals)) + powers[power] + suffix
        else:
            result = str(round(number, decimals)) + '.'
        return sign + (result[::-1].zfill(decimals + len(result)))[::-1] + powers[power] + suffix



if __name__ == '__main__':
    assert checkio_common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio_common_words("one,two,three", "four,five,six") == "", "Too different"
    assert checkio_common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M'
    assert friendly_number(102, decimals=2) == '102.00'
    assert friendly_number(-150, base=100, powers=["","d","D"]) == '-1d'
    assert friendly_number(-155, powers=["","d","D"], base=100, decimals=1) == '-1.6d'
    assert friendly_number(255000000000, powers=["","k","M"]) == '255000M'
    assert friendly_number(0, decimals=3, suffix="th") == '0.000th'