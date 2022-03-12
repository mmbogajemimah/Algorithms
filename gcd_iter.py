a = 2
b = 12

def itergcd(a, b):
    number = 0
    if a<b:
        number = a
    else:
        number = b 
    for i in range(1, number+1):
            if ((a%i == 0) and (b%i == 0)):
                gcd = i
    return gcd
print(itergcd(2, 12))
    

