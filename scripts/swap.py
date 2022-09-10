def swap_elements(input_list, x, y):
    """
    Swaps the value of the element x and element y
    using no more variables! Just a hack I like :)
    """
    valX = input_list[x]
    valY = input_list[y]
    
    valX = valX - valY
    valY = valX + valY
    valX = valY - valX
    
    #We had to separate the procedure because we are working with lists
    
    input_list[x] = valX
    input_list[y] = valY