descend_counter = 0


def check_descend(input_list):
    global descend_counter
    flag = 0
    if descend_counter <= 1:
        descend_counter = descend_counter + 1
        for i in range(len(input_list)-1):
            if i == len(input_list) - 1:
                break
            else:
                print(input_list[i], 'Next ', input_list[i+1])
                if int(input_list[i]) > int(input_list[i+1]):
                    if 3 >= int(input_list[i]) - int(input_list[i+1]) > 0:
                        flag = 1
                    else:
                        print("Runs when the difference is out of range")
                        new_input = input_list[:]
                        new_input.pop(i+1)
                        print(new_input)
                        if check_descend(new_input):
                            flag = 1
                        else:
                            flag = 0
                else:
                    print('Runs when current is smaller than next')
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


line = [109, 99, 98, 97, 96, 94]
print(check_descend(line))
