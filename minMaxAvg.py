# enter the lenght of your list
readLenghtList = int(input("Enter the list lenght: "))

# declaring list
myList = []

# adding each element from user in a list
i = 0
while i < readLenghtList:
    number = int(input("Enter element: "))
    myList.append(number)
    i += 1



# function for min
def min(list):

    min = list[0]
    i = 0
    # find the min compared to other numbers
    while i < len(list):
        if list[i] < min:
            min = list[i]
        i += 1
    print("Min = ", min)

# function for max
def max(list):
    max = list[0]
    i = 0
    #find the max compared to other numbers
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    print("Max = ", max)

# functon for average
def average(list):
    result = 0
    i = 0
    while i < len(list):
        result += list[i] 
        
        i += 1
    print("Average = ", result / len(list))
    


min(myList)
max(myList)
average(myList)







