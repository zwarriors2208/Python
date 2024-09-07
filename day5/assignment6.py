"""checks the use of try and except blocks"""

def get_integer_input():
    '''checks if the input is integer'''
    try :
        a = int(input("Enter a number: "))
        print("the try of get_integer_input was success")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def get_element_from_list(l):
    """checks for valid syntax"""
    # the argument l is list
    a1 = input("Enter a index of list you want to search: ")
    try:
        print(l[a1])
    except IndexError:
        print("Invalid input. Please enter a valid index.")
    except TypeError:
        print("Invalid input. Please enter a integer.")
    else:
        print("error ;(")

def divide_number(a, b):
    # if b == 0:
    #     raise ZeroDivisionError
    try:
        print("the division is:", a/b)
    except ZeroDivisionError:
        print("Division by zero")

# get_integer_input()
# l = [1,2,3,4,5,6]
# get_element_from_list(l)
# divide_number(2,3)
# divide_number(4,0)


print(__doc__)
print(get_element_from_list.__doc__)
help(get_integer_input)



# get_integer_input()