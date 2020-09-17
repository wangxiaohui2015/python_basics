import re

str = "www.google.com, https://www.baidu.com/, www.qq.com, https://www.amazon.com"
result = re.findall('www\..*?\.com', str)
for r in result:
    print(r)
