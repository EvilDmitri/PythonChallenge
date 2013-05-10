from collections import OrderedDict

my_dict = OrderedDict()

with open('data.txt') as f:

    for line in f.readlines():
        for char in line:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1

ready = []
for key in my_dict.keys():
    if my_dict[key] == 1:
        ready.append(key)

print(''.join(ready))