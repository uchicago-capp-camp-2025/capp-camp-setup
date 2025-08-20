# 4: IndentationError
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
    if letter in vowels:
    count += 1
    return count
