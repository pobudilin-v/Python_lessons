import random
num_size = random.randint(3, 10)
numbers = []
for _ in range(num_size):
    numbers.append(random.randint(1,50))
print(numbers)
index = [0, 2, len(numbers)-1]
newlist = []
for i in index:
    newlist.append(numbers[i])
print(newlist)





