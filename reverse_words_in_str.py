"""
151. Reverse Words in a String
Difficulty: Medium
Topics: ["Two Pointers", "String"]

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
"""

def reverse_words(s: str) -> str:
    res = list(filter(
        lambda x: (x != "" and not x.isspace()),
        s.split(" ")
        ))
    return " ".join(res[::-1])
