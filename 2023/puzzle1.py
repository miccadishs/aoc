import re

file_object = open('../input.txt', 'r')
total = 0
file_data = file_object.read()

lines = file_data.splitlines()

print(lines)

file_object.close()

for x in lines:
    i = re.findall(r'\d+', x)
    j = ''.join(i)
    k = j[:1]
    l = j[-1:]
    result = int(k + l)
    print(result)
    total += result

print(total)
