x = int(input("Provide an X value: "))
epsilon = 0.001
number_of_guesses = 0
low = 0.0
high = x
ans = (low + high)/2.0

while abs(ans**2 - x)>= epsilon:
    print('Low: ' + str(low)  + ' High: ' +  str(high) + ' Ans: ' +  str(ans))
    number_of_guesses = number_of_guesses + 1
    if ans**2 < x:
        low = ans
    else:
        high = ans

    ans = (low + high)/2.0

print("Number of guesses is: " + str(number_of_guesses))
print(str(ans) + 'is close to the square root of ' + str(x))