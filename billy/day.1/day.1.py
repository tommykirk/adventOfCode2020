# https://adventofcode.com/2020/day/1

import urllib

link = "http://adventofcode.com/2020/day/1/input"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)