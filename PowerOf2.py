def power2(number):
    if number <= 0:
        return False
    return(number & (number - 1)) == 0
n = int(input("Enter your number:"))
if power2(n):
    print(n,"is a power of 2")
else:
    print(n,"is not a power of 2")