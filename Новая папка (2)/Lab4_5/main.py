import re

s = input("Введите текст: ")

ns = re.findall(r'[A-Z]\w+[0-9]{2}\b', s)

print(ns)