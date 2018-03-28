
# Say Hi
def say_hi(name, age):
    return 'Hi. My name is ' + str(name) + " and I'm " + str(age) + ' years old'


# Correct Sentence
def correct_sentence(text: str) -> str:
    return (text[0].upper() + text[1:len(text)] + '.').replace('..', '.')


# First Word
def first_word(text: str) -> str:
    return text.strip(',. ').replace(',', '').split(' ')[0]


# Second index
def second_index(text: str, symbol: str):
    i = (text.replace(text[text.find(symbol)], '', 1)).find(symbol)
    if i == -1:
        return None
    else:
        return i + 1


# Beetwen Markers
def between_markers(text: str, begin: str, end: str) -> str:
    index_of_begin = text.find(begin)
    index_of_end = text.find(end)
    if index_of_begin < 0:
        index_of_begin = 0
    else:
        index_of_begin += len(begin)
    if index_of_end < 0:
        index_of_end = len(text)
    return text[index_of_begin:index_of_end]


# Best Stock
def best_stock(data):
    best = max(data.values())
    for key in data:
        if data[key] == best:
            return key


# Popular words
def popular_words(text, words):
    return {word: text.lower().count(word) for word in words}


# Bigger Price
def bigger_price(limit, data):
    return sorted(data, key=lambda dicts: dicts['price'], reverse=True)[:limit]


# Fizz Buzz
def checkio_fizz_buzz(number):
    res3, res5 = number % 3, number % 5
    if (res3 == 0) and (res5 == 0):
        s = "Fizz Buzz"
    elif not res3:
        s = 'Fizz'
    elif not res5:
        s = 'Buzz'
    else:
        s = str(number)
    return s


# The Most Numbers
def checkio_numbers(*args):
    if args:
        return max(args) - min(args)
    return 0


# Even The Last
def checkio_even(a):
    amount = 0
    if a:
        for x in range((len(a) // 2) + (len(a) % 2)):
            amount += a[x * 2]
        amount *= a[len(a) - 1]
    return amount


# Secret Message
def find_message(text):
    return ''.join([x for x in text if x.istitle()])


# Three Words
def checkio_words(words):
    words = words.split(' ')
    if [''.join(words[x:x + 3]).isalpha() for x in range(len(words) - 2)].count(True):
        return True
    return False


# Index Power
def index_power(array, n):
    if n <= (len(array) - 1):
        return array[n] ** n
    return -1


# Right To Left
def left_join(phrases):
    return ','.join(phrases).replace('right', 'left')


# Digits Multiplication
def checkio_multiplication(number):
    mp = 1
    for x in str(number):
        if int(x):
            mp *= int(x)
    return mp


# Number Base
def checkio_number_base(str_number, radix):
    while not None:
        try:
            return int(str_number, radix)
        except ValueError:
            return -1


# Adsolute Sorting
def checkio_sorting(numbers_array):
    return sorted(list(numbers_array), key=abs)


# The Most Frequent
def most_frequent(data):
    return sorted(data, key=lambda word: data.count(word), reverse=True)[0]


# Easy Unpack
def easy_unpack(elements):
    return elements[0], elements[2], elements[-2]


# Date And Time Convertor
def date_time(time):
    print(now)
    return time


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'

    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"

    assert popular_words('''
    When I was One,
    I had just begun.
    When I was Two,
    I was nearly new.
    ''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }

    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"
    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    assert checkio_fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio_fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert checkio_fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert checkio_fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"

    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio_numbers(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio_numbers(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio_numbers(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio_numbers(), 0, 3), "Empty"

    assert checkio_even([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio_even([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio_even([6]) == 36, "(6)*6=36"
    assert checkio_even([]) == 0, "An empty array = 0"

    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    assert checkio_words("Hello World hello") is True, "Hello"
    assert checkio_words("He is 123 man") is False, "123 man"
    assert checkio_words("1 2 3 4") is False, "Digits"
    assert checkio_words("bla bla bla bla") is True, "Bla Bla"
    assert checkio_words("Hi") is False, "Hi"

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"

    assert checkio_multiplication(123405) == 120
    assert checkio_multiplication(999) == 729
    assert checkio_multiplication(1000) == 1
    assert checkio_multiplication(1111) == 1

    assert checkio_number_base("AF", 16) == 175, "Hex"
    assert checkio_number_base("101", 2) == 5, "Bin"
    assert checkio_number_base("101", 5) == 26, "5 base"
    assert checkio_number_base("Z", 36) == 35, "Z base"
    assert checkio_number_base("AB", 10) == -1, "B > A = 10"

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio_sorting((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio_sorting((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio_sorting((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'
    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)

    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"