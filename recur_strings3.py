
def isIn(test_value, string):
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
                
        elif len(string) > 1:
            first = string[0]
            last = string[-1]
            middlevalue = len(string)//2
            if string[middlevalue] == test_value:
                return True
            else:
                if string[middlevalue] < test_value:
                    return isIn(test_value, string[middlevalue:])
                else:
                    return isIn(test_value, string[:middlevalue])
                
                
print(isIn('y', 'Python'))