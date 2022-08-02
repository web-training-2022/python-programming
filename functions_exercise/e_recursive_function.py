'''
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
'''
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        print (f"adding {n} to the sum")
        return n + sum_of_numbers(n-1)
        '''
        5 + sum_of_numbers(4) ==> 5 + 4 + 3 + 2 + 1 + 0
        4 + sum_of_numbers(3) ==> 4 + 3 + 2 + 1 + 0
        3 + sum_of_numbers(2) ==> 3 + 2 + 1 + 0
        2 + sum_of_numbers(1) ==> 2 + 1 + 0
        1 + sum_of_numbers(0) ==> 1 + 0
        '''

# example of recursive function
print(sum_of_numbers(5))
# print(sum_of_numbers(5 + 4 + 3 + 2 + 1 + 0))


'''
def bob(names):
    if names == []:
        return None
    print(f"Thank you {names[-1]}")
    names.remove(names[-1])
    print(f"calling bob with {names} -> {bob(names)}")
'''