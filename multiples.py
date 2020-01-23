def list_of_multiples(x, y):
    my_list = []
    for i in range(y):
        my_list.append(x*(i + 1))
    return my_list

print(list_of_multiples(12, 6))