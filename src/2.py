import string

def is_palindrome(text) -> bool | str:
    if not isinstance(text, str):
        return "Это не строка"
    filtered = ''.join(ch.lower() for ch in text if ch.isalnum())
    return filtered == filtered[::-1]

# Тесты
assert is_palindrome(True) == "Это не строка"
assert is_palindrome(False) == "Это не строка"
assert is_palindrome(12) == "Это не строка"
assert is_palindrome("0") == True
assert is_palindrome("gg") == True
assert is_palindrome("23kgrgl, efiisef, 9") == True
assert is_palindrome("Леша на полке нашел") == True
assert is_palindrome("Леша на полке нашел мышь!") == True
assert is_palindrome("pididi") == False
assert is_palindrome("glc") == False
