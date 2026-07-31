# Сделал в две стороны
import string
letters = input("Введите диапазон букв: ")
fletter = letters[0]
sletter = letters[2]
alphabet = string.ascii_letters
findex = alphabet.index(fletter)
sindex = alphabet.index(sletter)
if findex > sindex:
    result = alphabet[sindex : findex + 1][::-1]
else:
    result = alphabet[findex : sindex + 1]
print(result)