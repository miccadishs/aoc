file_object = open('test.txt', 'r')
file_data = file_object.read()
lines = file_data.splitlines()
result = list()
ascend_counter = 0
descend_counter = 0


def check_ascend(input_list):
    global ascend_counter
    a_flag = 0
    if ascend_counter <= 1:
        ascend_counter = ascend_counter + 1
        for i in range(len(input_list) - 1):
            if i == len(input_list) - 1:
                break
            else:
                # print(input_list[i], " Next : ", input_list[i+1])
                if int(input_list[i]) < int(input_list[i + 1]):
                    if 3 >= int(input_list[i + 1]) - int(input_list[i]) > 0:
                        a_flag = 1
                    else:
                        # print("Runs when the difference is out of range")
                        new_input = input_list[:]
                        new_input.pop(i+1)
                        # print(new_input)
                        if check_ascend(new_input):
                            a_flag = 1
                        else:
                            a_flag = 0
                else:
                    # print('Runs when current is bigger than next')
                    for x in range(len(input_list) - 1):
                        new_input = input_list[:]
                        new_input.pop(x)
                        if check_ascend(new_input):
                            a_flag = 1
                        else:
                            a_flag = 0
        match a_flag:
            case 0:
                return False
            case 1:
                return True
    else:
        return False


def check_descend(input_list):
    global descend_counter
    flag = 0
    if descend_counter <= 1:
        descend_counter = descend_counter + 1
        for i in range(len(input_list)-1):
            if i == len(input_list) - 1:
                break
            else:
                # print(input_list[i], 'Next ', input_list[i+1])
                if int(input_list[i]) > int(input_list[i+1]):
                    if 3 >= int(input_list[i]) - int(input_list[i+1]) > 0:
                        flag = 1
                    else:
                        # print("Runs when the difference is out of range")
                        new_input = input_list[:]
                        new_input.pop(i+1)
                        # print(new_input)
                        if check_descend(new_input):
                            flag = 1
                        else:
                            flag = 0
                else:
                    # print('Runs when current is smaller than next')
                    for x in range(len(input_list) - 1):
                        new_input = input_list[:]
                        new_input.pop(x)
                        if check_descend(new_input):
                            flag = 1
                        else:
                            flag = 0
        match flag:
            case 0:
                return False
            case 1:
                return True
    else:
        return False


for line in lines:
    ascend_counter = 0
    descend_counter = 0
    new_line = line.split()
    if check_ascend(new_line) or check_descend(new_line):
        if check_ascend(new_line):
            print('Ascending')
        elif check_descend(new_line):
            print('Descending')
        elif check_descend(new_line) and check_ascend(new_line):
            print('Conflict error')
        result.append(line)
print(result)
print(len(result))


