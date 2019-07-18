def list_binary_search_depth_2(list,value):
    if len(list) == 0:
        return [False, 0]

    elif len(list) == 1:
        return [list[0] == value, 0]

    else:
        if value == list[len(list)//2]:
            return [True, 0]
            
        if value<list[len(list)//2]:
            new_list = list[:len(list)//2]
        else:
            new_list = list[(len(list)//2)+1:]
            
        result, depth = list_binary_search_depth_2(new_list,value)
        return ([result, depth+1])
            
A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 24, 25]

print list_binary_search_depth_2(A,0)
print list_binary_search_depth_2(A,1)
print list_binary_search_depth_2(A,2)
print list_binary_search_depth_2(A,13)
print list_binary_search_depth_2(A,24)
print list_binary_search_depth_2(A,25)
print list_binary_search_depth_2(A,26)
