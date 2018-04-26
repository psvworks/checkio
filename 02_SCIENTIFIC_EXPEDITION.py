

# Common Words
def checkio_common_words(first, second):
    return ','.join(sorted([x for x in first.split(',') for y in second.split(',') if x == y]))


if __name__ == '__main__':
    assert checkio_common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio_common_words("one,two,three", "four,five,six") == "", "Too different"
    assert checkio_common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"