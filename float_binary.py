
x = float(input("Provide a number between 0 and 1: "))
power = 0
while ((2**power)*x) %1 != 0:
    print("Reminder = " + str((2**power)*x - int((2**power)*x)))
    power = power + 1

num = int(x*(2**power))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(power - len(result)):
    result='0' + result

result = result[0:-power] + '.' + result[-power:]
print("The binary represenntation of the decimal" + str(x) + 'is' + str(result))