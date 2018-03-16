# Say Hi
def say_hi(name, age):
    return 'Hi. My name is ' + str(name) + " and I'm " + str(age) + ' years old'


# Correct Sentence
def correct_sentence(text: str) -> str:
    return (text[0].upper() + text[1:len(text)] + '.').replace('..','.')


# First Word
def first_word(text: str) -> str:
    return text.strip(',. ').replace(',', '').split(' ')[0];


# Second index
def second_index(text: str, symbol: str):
    i = (text.replace(text[text.find(symbol)], '', 1)).find(symbol)
    if i == -1: return None
    else: return i + 1


# Beetwen Markers
def between_markers(text: str, begin: str, end: str) -> str:
    index_of_begin = text.find(begin)
    index_of_end = text.find(end)
    if index_of_begin < 0: index_of_begin = 0
    else: index_of_begin += len(begin)
    if index_of_end < 0: index_of_end = len(text)
    return text[index_of_begin:index_of_end]


# Best Stock
def best_stock(data):
    best = max(data.values())
    for key in data:
        if data[key] == best: return key



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