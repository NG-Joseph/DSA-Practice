import time

def factorial(n, prev_result=None):
    if n == 0:
        return 1
    # multiply n * n-1
    if prev_result == None:
        result = n
    else:
        result = prev_result
    if (n != 1):
        result *= n-1
        n -= 1
        return factorial(n, result)


    return result


# Python program to find the factorial of a number provided by the user
# using recursion

def better_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        print(f"{x} * {better_factorial(x-1)}")
        # recursive call to the function

        return (x * better_factorial(x-1))


#print(factorial(4))
print(better_factorial(4))


def racer(func1, arg1, func2, arg2):
    st = time.time()
    func1(arg1)
    print(f"Time elapsed is {abs(st - time.time())}")
    st2 = time.time()
    func2(arg2)
    print(f"Time elapsed is {abs(st2 - time.time())}")



#racer(factorial,4, better_factorial,4)
