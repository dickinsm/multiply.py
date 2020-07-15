# Author: Makaliah Dickinson
# Date: 7/14/2020
# Description: Write a recursive function named multiply that takes two positive integers as parameters and returns the
#              product of those two numbers (the result from multiplying them together). Your program should not use
#              multiplication - it should find the result by using only addition.


def mult(n, m):
    if m == 0:
        return 0
    elif m < 0:
        return n - mult(n, m + 1)
    else:
        return n + mult(n, m - 1)


print(mult(5, 3))
