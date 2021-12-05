import re
s = input()
result = re.sub(r'And|and', r'&', s)
print(result)
