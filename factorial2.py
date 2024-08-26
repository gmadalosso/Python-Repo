#factorial solution using while loop
def factorial(num):

    if type(num) is int:
        if num < 0:
            return None
        else: 
            count = num
            fact = 1

            while count >= 2:
                fact *= count
                count -= 1
            
            return fact
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