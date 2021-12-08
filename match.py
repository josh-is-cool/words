
def count(letter, word):
    x = 0
    for l in word:
        if letter == l:
            x = x + 1
    return x

print(count("a","aardvark"))

def match(word1, word):
    for l in word1:
        if count(l,word) < count(l, word1):
            return False
    return True

print(match("aserthjar","aardvark"))
