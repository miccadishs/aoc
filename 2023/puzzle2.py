import re

file_object = open('../input.txt', 'r')
total = 0
file_data = file_object.read()
lines = file_data.splitlines()
fixed_line = list()
file_object.close()


def find_words_in_string(input_string):
    # Split items string into a set of words for quick lookup
    # item_words = set(items.split())
    replacement = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    found_words = []

    # Iterate through the input string
    #find a way to stop after find the first word
    for i in range(len(input_string)):
        # Check every possible substring starting from the current character
        for j in range(i + 1, len(input_string) + 1):
            # Extract substring
            substring = input_string[i:j]

            # Check if it's in the item_words
            if substring in replacement:
                found_words.append(substring)
            else:
                if input_string[i].isdigit():
                    if input_string[i] in found_words:
                        pass
                    else:
                        found_words.append(input_string[i])

    return replace_words_with_numbers(''.join(found_words))


def replace_words_with_numbers(input_string):
    # Mapping of number words to their numeric equivalents
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    # Result string to build
    result = ""
    current_word = ""

    # Iterate through the input string character by character
    for char in input_string:
        if char.isalpha():
            # Build the current word
            current_word += char
            # Check if the current word matches a number word
            if current_word in word_to_number:
                result += word_to_number[current_word]
                current_word = ""
        else:
            # If it's not a letter, append it directly to the result
            result += char

    # If any unmatched word remains, add it back (optional behavior)
    result += current_word

    return result


for line in lines:
    fixed_line.append(find_words_in_string(line))

total = 0
newline = list()
for x in fixed_line:
    k = x[:1]
    l = x[-1:]
    newline.append(int(k + l))


print(sum(newline))

