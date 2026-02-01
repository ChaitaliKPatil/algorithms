# sum of the first N numbers
# 1: parameterized way
# 2: functional way

# 1: parameterized way ==> adding/carrying the result to the parameters
def sum_f(i, summ):
    if i < 1:
        print(summ)
        return
    summ += i
    sum_f(i-1, summ)

N = 3
sum_f(N, 0)




# 2: functional way ==> carrying results by returning it.
def sum_f(n):
    if n == 0: return 0
    return n + sum_f(n-1)

N = 10
res = sum_f(N)
print(res)




