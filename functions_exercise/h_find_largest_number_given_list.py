input_list = [1,2,3,4,5,6,7,8,9,12,13,15,17]

def max_rec(input_list):
    if not isinstance(input_list,list) \
       or (isinstance(input_list,list) and len(input_list) == 0) :
        return "Invalid input given to function"
    if len(input_list) == 1:
        return input_list[0]
    else:
        if input_list[0] <= input_list[-1]:
            input_list.remove(input_list[0])
        else:
            input_list.remove(input_list[-1])
        max_rec(input_list)