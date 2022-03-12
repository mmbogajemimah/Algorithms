x = int(input("Provide an X: "))
epsillon = 0.0001
number_of_guesses = 0
low = 0.0
high = x
ans = (low + high)/2.0

while abs(ans**3 - x)>= epsillon:
    print("Low = " + str(low) + "High = " + str(high) + "Ans = " + str(ans))
    number_of_guesses = number_of_guesses + 1
    if ans**3 < x:
        low = ans
    else:
        high = ans

    ans = (low + high)/2.0

print("Number of guesses: " + str(number_of_guesses))
print(str(ans) + "is close to the cube root of " + str(x))


num = int(input("Provide a number: "))
result = ''

if num < 0:
    num = abs(num)
else:
    num = num

if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num//2
if num < 0:
    result = '-' + result
print(result)