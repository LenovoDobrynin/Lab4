import re
s = input()
res = re.sub(r'And|and|ANd|AnD|aND|anD|AND|aNd', r'&', s)
result = re.sub(r'Or|or|OR|oR', r'|',res)
print(result)
