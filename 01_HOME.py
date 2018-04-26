import re
from typing import List, Any


# House Password
def checkio_house_password(data):
    sec = True
    if data.isalpha():
        sec = (sec and False)
    if data.isdigit():
        sec = (sec and False)
    if data.isupper():
        sec = (sec and False)
    if data.islower():
        sec = (sec and False)
    if len(data) < 10:
        sec = (sec and False)
    return sec


# The Most Wanted Letter
def checkio_the_most_wanted_letter(text):
    text = text.lower()
    s = sorted([x for x in set(text) if x.isalpha()])
    maximum, ch = 0, s[0]
    for x in s:
        if text.count(x) > maximum:
            maximum = text.count(x)
            ch = x
    return ch


# Non-unique Elements
def checkio_nonunique_elements(data):
    return [x for x in data if data.count(x) > 1]


# Monkey Typing
def count_words(text, words):
    return len([word for word in words if text.lower().count(word) > 0])


# Xs and Os Referee
def checkio_referee(game_result):
    r = len(game_result)-1              # ранг матрицы
    win = "D"
    diag = ''
    y = -1
    for x in game_result:
        if x.count(x[0]) > r:
            win = x[0]
        y += 1
        diag += x[y]
    if diag.count(diag[0]) > r:
        win = diag[0]

    transp_result = list(zip(*game_result[::-1]))
    diag = ''
    y = -1
    for x in transp_result:
        if x.count(x[0]) > r:
            win = x[0]
        y += 1
        diag += x[y]
    if diag.count(diag[0]) > r:
        win = diag[0]
    if win == '.':
        win = "D"
    return win


# Pawn Brotherhood
def safe_pawns(pawns):
    return len({pawn for pawn in pawns if ((chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns) or
                                           (chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)) in pawns)})


# Min and Max
'''
def min(*args, **kwargs):
    if len(args) == 1:
        return sorted(args[0], key = kwargs.get("key"))[0]
    return sorted(args, key=kwargs.get("key"))[0]


def max(*args, **kwargs):
    if len(args) == 1:
        return sorted(args[0], key = kwargs.get("key"), reverse=True)[0]
    return sorted(args, key=kwargs.get("key"), reverse=True)[0]
'''


# Long Repeat
def long_repeat(line):
    if line:
        return max(set(len(symbol*num) for symbol in set(line) for num in range(len(line)+1) if symbol*num in line))
    return 0
    #return len(line) and 1+long_repeat(''.join(u for u,v in zip(line,line[1:]) if u==v))


# All the Same
def all_the_same(elements: List[Any]) -> bool:
    if len(set(elements)) > 1:
        return False
    return True


if __name__ == '__main__':
    assert checkio_house_password('A1213pokl') == False, "1st example"
    assert checkio_house_password('bAse730onE4') == True, "2nd example"
    assert checkio_house_password('asasasasasasasaas') == False, "3rd example"
    assert checkio_house_password('QWERTYqwerty') == False, "4th example"
    assert checkio_house_password('123456123456') == False, "5th example"
    assert checkio_house_password('QwErTy911poqqqq') == True, "6th example"

    assert checkio_the_most_wanted_letter("Hello World!") == "l", "Hello test"
    assert checkio_the_most_wanted_letter("How do you do?") == "o", "O is most wanted"
    assert checkio_the_most_wanted_letter("One") == "e", "All letter only once."
    assert checkio_the_most_wanted_letter("Oops!") == "o", "Don't forget about lower case."
    assert checkio_the_most_wanted_letter("AAaooo!!!!") == "a", "Only letters."
    assert checkio_the_most_wanted_letter("abe") == "a", "The First."
    assert checkio_the_most_wanted_letter("a" * 9000 + "b" * 1000) == "a", "Long."

    assert list(checkio_nonunique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio_nonunique_elements([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio_nonunique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio_nonunique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"

    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    assert checkio_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True