from merge_str_alt import merge_alternatively, merge_alternatively2

def test_both_words_have_equal_length():
    assert merge_alternatively("abc", "pqr") == "apbqcr"


def test_word1_is_longer():
    assert merge_alternatively("ab", "pqrs") == "apbqrs"


def test_word2_is_longer():
    assert merge_alternatively("abcd", "pq") == "apbqcd"


def test_word1_is_empty():
    assert merge_alternatively("", "pqrs") == "pqrs"


def test_word2_is_empty():
    assert merge_alternatively("abcd", "") == "abcd"


def test_f2_both_words_have_equal_length():
    assert merge_alternatively2("abc", "pqr") == "apbqcr"


def test_f2_word1_is_longer():
    assert merge_alternatively2("ab", "pqrs") == "apbqrs"


def test_f2_word2_is_longer():
    assert merge_alternatively2("abcd", "pq") == "apbqcd"


def test_f2_word1_is_empty():
    assert merge_alternatively2("", "pqrs") == "pqrs"


def test_f2_word2_is_empty():
    assert merge_alternatively2("abcd", "") == "abcd"

