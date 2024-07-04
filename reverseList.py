array = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(input_list):
    reversed_list = []
    for i in input_list[::-1]:
        if isinstance(i, list):
            reversed_list.append(reverse_list(i))
        else:
            reversed_list.append(i)
    return reversed_list

array = reverse_list(array)
print(array)





    
