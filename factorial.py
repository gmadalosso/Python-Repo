def factorial(num):

    if type(num) is int:
        if num < 2 and num >= 0:
            return 1
        elif num < 0:
            return None
        else:
            return num * factorial(num - 1)
    else:
        return None
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))
print(factorial(1.2))
print(factorial('string'))