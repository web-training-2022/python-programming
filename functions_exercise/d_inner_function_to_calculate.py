'''
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
'''

def new_function(name,age=0):
    print(f"{name} is registred with age={age}")

    def eligible_vote(age):
        if age >= 18:
            return True
        else:
            return False
    if eligible_vote(age):    
        print(f"{name} is eligible to vote")
    else:
        print(f"{name} is NOT eligible to vote")

new_function("Dinesh", 29)