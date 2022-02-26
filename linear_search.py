#Initialize a target
target = int(input("Provide an integer: "))
#Initialize a list
count = int(input("How long do you want your list to be: "))
numbers = []
#A Loop to get the list
for i in range(count):
    num = int(input("Provide a number:"))
    numbers.append(num)
print(numbers)

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("The target value is found in the list", index)
    else:
        print("The Target value is not found in the list")

result = linear_search(numbers, target)
verify(result)