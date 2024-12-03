ascend_counter = 0


def check_ascend(input_list):
    global ascend_counter
    a_flag = 0
    if ascend_counter <= 1:
        ascend_counter = ascend_counter + 1
        for i in range(len(input_list) - 1):
            if i == len(input_list) - 1:
                break
            else:
                print(input_list[i], " Next : ", input_list[i+1])
                if int(input_list[i]) < int(input_list[i + 1]):
                    if 3 >= int(input_list[i + 1]) - int(input_list[i]) > 0:
                        a_flag = 1
                    else:
                        print("Runs when the difference is out of range")
                        new_input = input_list[:]
                        new_input.pop(i+1)
                        print(new_input)
                        if check_ascend(new_input):
                            a_flag = 1
                        else:
                            a_flag = 0
                else:
                    print('Runs when current is bigger than next')
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


line = [73, 76, 79, 80, 81, 84, 86, 86]
print(check_ascend(line))

