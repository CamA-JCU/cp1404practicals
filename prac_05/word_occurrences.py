"""
CP1404/CP5632 Practical
Count the occurrences of words in a string.
"""

words_to_count = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

# print each word sorted alphabetically with it's word count
words = list(words_to_count.keys())
words.sort()
for word in words:
    print(f"{word} : {words_to_count[word]}")
