import re

x = 'My 2 favorite numbers are 19 and 42'
z = 'From Using the : character'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[aeiou]+', x)
print(y)
# greedy matching, matches all characters
y = re.findall('^F.+:', z)
print(y)
