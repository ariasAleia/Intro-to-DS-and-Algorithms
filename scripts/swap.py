def swap_elements(input_list, x, y):
    """
    Swaps the value of the element x and element y
    using no more variables! Just a hack I like :)
    """
    input_list[x] = input_list[x] - input_list[y]
    input_list[y] = input_list[x] + input_list[y]
    input_list[x] = input_list[y] - input_list[x]