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

old_function = new_function
old_function("Dinesh", 29)

print(type(old_function) )
print(type(new_function) )
