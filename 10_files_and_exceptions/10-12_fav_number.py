import json

# 10.11/10.12 - Write a program that prompts the user for the user's favorite number.
# Use json.dump() to store this number in a file. Then give that number back to the user.

def get_fav_number():
    '''Retrieves favorite number from memory if its exists.'''
    filename = 'fav_num.json'
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return num

def get_new_num():
    '''Prompt user for a new number.'''
    num = input("What's your favorite number? ")
    filename = 'fav_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)

def read_num():
    '''Give the favorite number away.''' 
    num = get_fav_number()
    if num:
        print("I know your favorite number! It's " + str(num) + ".")
    else:
        num = get_new_num()
        print("Got it, your favorite number is " + str(num) + ".")

read_num()

