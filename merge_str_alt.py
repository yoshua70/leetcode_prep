import itertools


def merge_alternatively(word1: str, word2: str):
    res = ""
    for (x, y) in itertools.zip_longest(word1, word2, fillvalue=""):
        res += x + y
    return res


def merge_alternatively2(word1: str, word2: str):
    # We need the length of the smallest string 
    # and all the characters of the longest ones.
    s_size = len(word1)
    l_str = word2
    if len(word1) > len(word2):
         s_size = len(word2)
         l_str = word1
         
    res = ""

    # Iterate over two lists until the smallest one is over.
    for (x, y) in zip(word1, word2):
        res = res + x + y

    # Append the remaining characters from the longest word to the result.
    res += l_str[s_size:]
    return res

