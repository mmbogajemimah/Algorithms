#Request for a target variable
target = int(input("Provide the target value: "))
# Request for the length of the list
length_list= int(input("Provide the length of your list: "))

# Initialize a list for the numbers
numbers = []
#  Use a for loop to run through the range of the length of the list requesting for input values
for i in range(length_list):
    num=int(input("Provide a number for your list: "))
    #Append the values given to the numbers list initilized
    numbers.append(num)
print(numbers)

def binary_search(numbers, target):
    first = 0
    last = len(numbers)-1
    #Calculating the middle value
    while first <= last:
        middle_value = (first + last)//2
        if numbers[middle_value] == target:
            return middle_value
        elif numbers[middle_value] < target:
            first = middle_value + 1
        else:
            last = middle_value - 1
    return None


def verify(index):
    if index is not None:
        print("The target value is found in the list: ", index)
    else:
        print("The target value is not found in the list")

result = binary_search(numbers, target)
verify(result)

#Define the Binary search function
#Keep track on the first value using its index in the list
#Keep track on the last value using its index in the list
#Calculate the middle value of the list
#if the middle value is less than the target value
#else

#Define a verify function
#if index is not in None ("Print sth")
#elif (Print sth)
