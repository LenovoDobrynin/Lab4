s = input("Введите предложение: ")
ns = {}

for el in s:
    if el in ns:
        ns[el] += 1
    else:
        ns[el] = 1

print ([el for el in ns if ns[el] == 1])