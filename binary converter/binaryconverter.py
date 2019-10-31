
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
    temp = []
    while number > 0:
        rest = number % 2
        number //= 2
        temp.append(str(rest))
    str1 = ''.join(temp)  
    return str1[::-1]

# get 2 numbers from user
first_number, second_number = input("Enter 2 numbers: ").split()

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
    if check_if_is_binary() == True and second_number == '2' or check_if_is_binary() == False and second_number == '2':
        conversion = convert_from_binary(int(first_number))
        print("{0} {1}".format(conversion, 10))
    elif check_if_is_binary() == False and second_number == '10' or check_if_is_binary() == True and second_number == '10':
        conversion = convert_from_decimal(int(first_number))
        print("{0} {1}".format(conversion, 2))
    else:
        print("You didn't enter as instructed")

make_conversion()

