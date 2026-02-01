# 1: parameterized way ==> adding/carrying the result to the parameters
N = 5
def fact(n, prod):
    if n == 1:
        print(prod)
        return 1
    fact(n-1, prod*n)
fact(N, 1)


def fact(n, prod):
    if n == 1:
        print(prod)
        return 1
    n = n-1
    prod *= n
    fact(n, prod)
fact(N+1, 1)


# 2: functional way ==> carrying results by returning it.
def fact(n):
    if n == 1: return 1
    return n * fact(n-1)
fact(N)