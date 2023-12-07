# Task 1 practice - Collatz + while loop

x = 5

def f(x):
    #if x is even, devide with 2
    if x %2 == 0:
        return x / 2
    else:
        return (3 * x) +1

while x>1:
    x=int(f(x))
    print(x)