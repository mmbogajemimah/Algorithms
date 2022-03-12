#string = "Python"


#print(string)
#test_value = 'y'
#middle_value = len(string)//2
#print(middle_value)

def isIn (test_value, string):
    #test_value = "y"
    string = string.lower()
    string = ''.join(sorted(string))
    if len(string) == 0:
        return False
    elif len(string) > 0:
        if len(string) == 1:
            if string == test_value:
                return True
            else:
                return False

        if len(string) > 1:
            first = string[0]
            last = string[-1]

            middle_value = len(string)//2

            if string[middle_value] == test_value:
                return True
            for i in range(1, len(string)-1):
                if string[middle_value] < test_value:
                    first = string[middle_value]
                    string = string[middle_value:]
                    middle_value = len(string)//2
                    if string[middle_value] == test_value:
                        return string[middle_value]
                elif string[middle_value] > test_value:
                    last = string[middle_value]
                    string = string[:middle_value]
                    middle_value = len(string)//2
                    if string[middle_value] == test_value:
                        return string[middle_value]

        return string[middle_value]

print(isIn ('a', 'Jemiahmbog'))
