array = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(input_list):
    flat_list = []
    for i in input_list:
        if isinstance(i,list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list
            
array = flatten_list(array)
print(array)
