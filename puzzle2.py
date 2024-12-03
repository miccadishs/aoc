
file_object = open('input2.txt', 'r')
file_object2 = open('input.txt', 'r')
file_data = file_object.read()
file_data2 = file_object2.read()
numbers = file_data.split()
numbers2 = file_data2.split()
results = list()

for x in numbers:
    occ = numbers2.count(x)
    results.append(int(x) * occ)

print(sum(results))
