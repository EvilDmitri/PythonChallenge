import pickle

text = pickle.load(open('banner.p', 'rb'))

for item in text:
    print "".join(e[1]*e[0] for e in item)