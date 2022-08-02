'''
Write a program to create a function that 
takes two arguments, name and age, 
and print their value.
'''

def arg_function(name,age):
    print(f"name: {name[:19]: <20} age: {age[:10]: <10}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age  = input("Enter your age: ") 
    name1 = input("Enter your name: ")
    age1  = input("Enter your age: ") 
    arg_function(name,age)
    arg_function(name1,age1)