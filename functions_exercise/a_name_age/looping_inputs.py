names = []
ages = []

if __name__ == "__main__":
    n = input("Enter number of entries you want to make: ")
    for i in range(int(n)):
        name = input("Enter name: ")
        names.append(name)
        age = input("Enter age: ")
        ages.append(age)
    
    print ("\n")
    print (f"{'Name' : <15},{'Age' : <15}")
    for i in range(int(n)):
        print (f"{names[i]: <15},{ages[i]:<15}")
        