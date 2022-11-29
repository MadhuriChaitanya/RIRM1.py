import re

numbers = [
'2124567890',
'212-456-7890',
'212.456.7890',
'(212)456-7890',
'(212)-4567890',
'212 456 7890',
'+12124567890',
'+1 212.456.7890',
'+212-456-7890',
'1-212-456-7890',
'2124567890'
]
pattern = re.compile(r'^(\+?\d?[ -]?)?(\()?(\d){3}(\))?([-. ])?(\d){3}([-. ])?(\d){4}$')
for x in  numbers:
matching = pattern.match(x)
if(matching is None):
print(x, is invalid)
elif(matching.group(2)!=matching.group(4) or matching.group(5)!=matching.group(7)):
print(x, is invalid)
else:
print(x, ' is valid')

