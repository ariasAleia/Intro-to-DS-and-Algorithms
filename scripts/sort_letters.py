def sort_letters(string):
    odd_numbers = ""
    even_numbers = ""
    lower_case = ""
    upper_case = ""
    ans = ""
    for letter in string:
        if letter in "13579":
            odd_numbers += letter
        elif letter in "02468":
            even_numbers += letter
        elif letter.isupper():
            upper_case += letter
        elif letter.islower():
            lower_case += letter

    ordered_list = sorted(lower_case) + sorted(upper_case) + sorted(odd_numbers) + sorted(even_numbers)
    
    for element in ordered_list:
        ans += element
    
    return ans
        

def main():
    print(sort_letters("2340Sorting1234"))
    
if __name__ == '__main__':
    main()