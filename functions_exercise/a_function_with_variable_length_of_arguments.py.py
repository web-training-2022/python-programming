#return multiple values from a function


def print_names(*values):
    for value in values:
        print(value)
    return None

print_names('ram','sham')

print_names('ram','sham', 'sumit', 'amit', 'dinesh', 'poonam')


