def sum_string(num_str):
    num_str = num_str.replace(" ", "").replace("+", "")
    
    num_list = [int(i) for i in num_str]

    num_sum = sum(num_list)

    num_int = int(num_sum)

    return num_int
num_str = "2+3"

num_int = sum_string(num_str)
print(num_int)

