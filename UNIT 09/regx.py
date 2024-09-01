import re

text = "Hello My name is Mehdi Abbas , Hello my name is Mehdi Abbas "
matches = re.search('Mehdi',text)
print(matches)

print(matches.span())
print(matches.start())
print(matches.end())
print("\n")
matches = re.findall('Mehdi',text)
for i in matches :
    print(i)
print("\n")
for matchs in re.finditer("Mehdi",text):
    print(matchs.group())
    print(matchs.span())
