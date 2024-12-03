from numpy import sort

file_object = open('input2.txt', 'r')
file_object2 = open('input.txt', 'r')
file_data = file_object.read()
file_data2 = file_object2.read()
numbers = file_data.split()
numbers2 = file_data2.split()
numbers.sort()
numbers2.sort()
result = list()

for i in range(0, len(numbers)):
    result.append(abs(int(numbers[i]) - int(numbers2[i])))


print(sum(result))



