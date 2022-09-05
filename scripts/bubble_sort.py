#Bubble sort
#My own implementation :)

def swap_elements(list, x, y):
    """
    Swaps the value of the element x and element y
    using no more variables! Just a hack I like :)
    """
    list[x] = list[x] - list[y]
    list[y] = list[x] + list[y]
    list[x] = list[y] - list[x]

def bubble_sort(list):
    index = 0
    current_limit = len(list) - 1
    
    while current_limit > 0:
        while index < current_limit:
            if(list[index] > list[index + 1]):
                swap_elements(list, index, index + 1)
            index+=1
        current_limit-=1
        index = 0    

def main():
    f = [9, -2 , 14, 67, 3, 8, 5, 2, 1, 0]
    bubble_sort(f)
    print(f)

if __name__ == '__main__':
    main()