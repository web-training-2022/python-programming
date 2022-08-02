def returning_values(num):
    list_num = []
    while num > 0:
        list_num.append(num)
        num -= 1
    return list_num, len(list_num)

output, length_of_output = returning_values(6)
print(f"output={output} & length={length_of_output}")

whole_output = returning_values(6)
print(f"complete output = {whole_output} and type={type(whole_output)}")