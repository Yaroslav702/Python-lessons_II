# def func(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return b + func(b+1, a)
#     return a + func(a+1, b)


# print(func(10, 5))

def fibo(x):
    if x <= 1:
        return x
    return fibo(x-1) + fibo(x-2)



# x, y = 1, 1
# a = int(input())
# a -= 2

# while a > 0:
#     x, y = y, x+y
#     a -= 1

# print(y)

def accerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return accerman(m-1, 1)
    return accerman(m-1, accerman(m, n-1))

print(accerman(1, 3))
