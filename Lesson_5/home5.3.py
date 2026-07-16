import string
text = input("Введите слова для хэштега:")
for char in string.punctuation:
    text = text.replace(char, " ")
words = text.split()
result = ""
for word in words:
    result += word.capitalize()
hashtag = "#" + result
print(hashtag)