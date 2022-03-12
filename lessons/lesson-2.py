# def palindrome(n):
#     if n[::-1] == n:
#         return "YES"
#     return "NO"

def palindrome(str):
    if not str:
        return True
    if str[0] != str[-1]:
        return False
    return palindrome(str[1:-1])


# def sequence(n):
#     j = 1
#     for i in range(1, n + 1):
#         print(j)
#         if i == j*(j + 1) // 2:
#             j += 1


