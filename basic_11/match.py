import re

str = "www.google.com"
match = re.match("www", str)
print(match)

match = re.match("google", str)
print(match)
