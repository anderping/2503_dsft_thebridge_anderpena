import calendar


week_days = list(calendar.day_name)

def get_week_day(num):
    return calendar.day_name[num]


def build_pyramid(rows):
    numbers = list(range(rows))
    print(type(numbers))

    for i in range(rows):
        print(f"{" ".join(map(str, numbers))}")

        del numbers[0]


def compare(a, b):
    if a == b:
        print("Los números son iguales")

        return
    
    elif a > b:
        print("a es mayor que b")
        
        return
    
    else:
        print("a es menor que b")
        
        return
    
    
def count_letters(text, letter):
    text = text.lower()
    letter = letter.lower()

    count = 0

    for x in text:
        if x == letter:
            count += 1

    return count


def count_letters_2(text):
    letter_dict = {}

    for letter in text:
        key = letter
        value = 1

        if key not in letter_dict:
            letter_dict[key] = value

        else:
            letter_dict[key] += 1


    return letter_dict


def change_list(list_6, function, element=None):
    if function == "add":
        list_6.append(element)
    
    elif function == "remove":
        list_6.remove(element)

    else:
        print("non existent function")

    return list_6


def build_sentence(*args):
    return " ".join(args)


def get_fib_number(n):
    if n == 0:
        return 0
    
    elif n < 0:
        print("Not a valid number")
        
        return None

    elif n == 1 or n == 2:
        return 1

    else:
        return get_fib_number(n-1) + get_fib_number(n-2)
    

import math


def calculate_square_area(a):
    return a**2

def calculate_triangle_area(a, b):
    return a*b

def calculate_circle_area(r):
    return math.pi*r**2