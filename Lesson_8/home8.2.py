def is_palindrome(text):
    text = text.lower()
    new_text = ""
    for symbol in text:
        if symbol.isalpha():
            new_text += symbol
    if new_text == new_text[::-1]:
        return True
    else:
        return False