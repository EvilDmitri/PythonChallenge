"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import zipfile

zf = zipfile.ZipFile('channel.zip')

text = zf.read('90052.txt')
print text
print zf.getinfo('90052.txt').comment
next_nothing = text.split(' ')[-1]


# def print_info(archive_name):
#     zf = zipfile.ZipFile(archive_name)
#     for info in zf.infolist():
#         print '\tComment:\t', info.comment
#
#
# print_info('channel.zip')

comments = []

while True:
    filename = next_nothing + '.txt'
    try:
        text = zf.read(filename)
    except KeyError:
        break
    next_nothing = text.split(' ')[-1]
    # print text
    comment =  zf.getinfo(filename).comment
    if comment == '*':
        pass
    else:
        if comment in comments:
            pass
        else:
            comments.append(comment)

print comments