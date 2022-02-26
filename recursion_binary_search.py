#Request for a target variable
target = int(input("Provide the target value: "))

# Request for the length of the list
length_list= int(input("Provide the number of values in your list: "))

# Initialize a list for the numbers
numbers = []
def list_numbers():
    for i in range(length_list):
        num=int(input("Provide a number for your list: "))
    #Append the values given to the numbers list initilized
        numbers.append(num)
    return numbers

#Define the recursion binary search
def recursion_binary_search(numbers, target):
    if len(numbers) == 0:
        return False
    else:
        midpoint = len(numbers)//2
        if numbers[midpoint] == target:
            return True
        elif numbers[midpoint] < target:
            return recursion_binary_search(numbers[midpoint+1 :], target)
        elif numbers[midpoint] > target:
            return recursion_binary_search(numbers[: midpoint], target)

numbers = list_numbers()
def verify(result):
     print("Target Found: ",result)

result = recursion_binary_search(numbers, target)
verify(result)

