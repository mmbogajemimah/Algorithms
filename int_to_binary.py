num = 3
result = ''


if num < 0:
    num = abs(num)
else:
    num = num

if num == 0:
    result = ''
while num > 0:
    result = str(num%2) + result
    num = num//2
if num < 0:
    result = '-' + result

print(result)