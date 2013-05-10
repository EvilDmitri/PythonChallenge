import urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
number = 12345
while True:
    data = urllib2.urlopen(url + str(number))
    string = data.read()
    print string
    number = string.split(' ')[-1]

