import re

lines = []
with open('data.txt') as f:
    lines = f.readlines()

p = re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')

ready = []
for line in lines:
    a = re.findall(p, line)
    if a:
        ready.append(a[0][4])

print ''.join(ready)