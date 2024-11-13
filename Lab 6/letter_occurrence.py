# def letter_occurrence(input_string):
    # complete function implementation...

def letter_occurance(input_string):
    count = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    return count

print(letter_occurance("Amazing"))
print(letter_occurance("Always aim ambitiously"))