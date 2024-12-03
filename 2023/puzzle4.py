import re
from functools import reduce
from operator import mul

file_object = open('../input2.txt', 'r')
file_data = file_object.read()
line_data = file_data.splitlines()
file_object.close()
fixed_data = list()
power = list()

def find_sum(input_string):
    new_line = input_string.replace(":", ";").split(";")
    blue = list()
    red = list()
    green = list()
    for item in new_line:
        new_item = item.split(',')
        for x in new_item:
            value, key = x.split()
            x_new = {key: value}
            if key == "blue":
                blue.append(int(x_new[key]))
            elif key == "green":
                green.append(int(x_new[key]))
            elif key == "red":
                red.append(int(x_new[key]))

    power.append(max(blue) * max(green) * max(red))
    return

    # if any(num > 14 for num in blue) or any(num > 13 for num in green) or any(num > 12 for num in red):
    #     pass
    # else:
    #     return (new_line[0])


for line in line_data:
    find_sum(line)

print(sum(power))
















