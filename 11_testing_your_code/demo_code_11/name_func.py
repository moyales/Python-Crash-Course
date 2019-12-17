# A function that takes a first and last name, then returns neatly formatted name.
def get_formatted_name(first, last, middle=''):
    '''Generate a fully formatted full name.'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()