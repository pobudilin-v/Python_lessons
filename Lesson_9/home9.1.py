def popular_words(text, words):
    text = text.lower()
    text_words = text.split()
    result = {}
    for word in words:
        result[word] = text_words.count(word)
    return result