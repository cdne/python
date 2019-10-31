# get 2 numbers from user
instructions = '''
You need to enter a decimal or binary number and a desired number system (2 or 10)

Example: 11010 2
         231 10
         33 10
         11110011 2
'''
print(instructions)
first_number, second_number = input("Enter 2 numbers: ").split()

# convert from binary
def convert_from_binary(number):
    result, i = 0, 0
    lenght = len(str(number))
    while i < lenght:
        rest = number % 10
        number //= 10
        result += rest *(2 ** i)    
        i += 1
    return result
    
# convert from decimal
def convert_from_decimal(number):
    temporary_list = []
    while number > 0:
        rest = number % 2
        number //= 2
        temporary_list.append(str(rest))
    str1 = ''.join(temporary_list)  
    return str1[::-1]

# def try_again():

# check if first number is binary
def check_if_is_binary():
    flag = False
    counter = 0
    for get_char in first_number:
        if get_char == '0' or get_char == '1':
            counter += 1
            if counter == len(first_number):
                flag = True
            else:
                flag = False
    return flag

# converts from binary to decimal and decimal to binary           
def make_conversion():
    if check_if_is_binary() == True and second_number == '2' or check_if_is_binary() == True and second_number == '10':
        conversion = convert_from_binary(int(first_number))
        print("{0} {1}".format(conversion, 10))
    elif check_if_is_binary() == False and second_number == '10':
        conversion = convert_from_decimal(int(first_number))
        print("{0} {1}".format(conversion, 2))
    else:
        print("You didn't enter as instructed")


make_conversion()

