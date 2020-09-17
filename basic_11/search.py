import re

# Check if a string matches a regexp
str = "www.google.com"
match = re.search('g.*e', str)
print(match)
print(match.span())
print(str[match.start():match.end()])

print()
match = re.search('ag.*e', str)
if match:
    print("Match")
else:
    print("Not match")

print()
# Search and group
match = re.search('(g.*e)\.(com)', str)
if match:
    print(match.group(1))
    print(match.group(2))
else:
    print("Not match.")
