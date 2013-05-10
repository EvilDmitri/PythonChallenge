
from string import maketrans

with open('data.txt', 'r') as f:
    text = f.readline()

    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    outtab = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'.lower()

    trantab = maketrans(alp, outtab)

    print(text.translate(trantab))


alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
outtab = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'.lower()

trantab = maketrans(alp, outtab)

print('map'.translate(trantab))