import misc
import re

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def example_one():
    return part_one(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"])
def example_two():
    return part_two(["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"])

def part_two(inputtext):
    sum = 0
    if len(inputtext) <= 0:
        inputtext = misc.read_file("files/1_1.txt")
    for line in inputtext:
        first, last = get_first_and_last_digit_of_line_including_written(line)
        print(first+", "+last)
        sum += int(first+last)
    return sum
def part_one(inputtext):
    sum = 0
    if len(inputtext) <= 0:
        inputtext = misc.read_file("files/1_1.txt")
    for line in inputtext:
        first, last = get_first_and_last_digit_of_line(line)
        print(first+", "+last)
        sum += int(first+last)
    return sum
def get_first_and_last_digit_of_line(line):
    res = re.findall("(\d)", line)
    return res[0], res[len(res)-1]
def get_first_and_last_digit_of_line_including_written(line):
    res = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    for a, b in help_dict.items():
        res[:] = [x if x != a else b for x in res]
    return res[0], res[len(res)-1]
