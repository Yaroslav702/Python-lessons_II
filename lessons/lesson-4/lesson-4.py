# with open('lesson-4/task1.txt', 'a') as f:
#     while True:
#         answer = input("Enter: ")
#         if answer == "0":
#             break
#         f.write(answer + '\n')


# a = input("Enter string: ")
# print(set(a))



# a = set(input())
# b = set(input())
# c = set(input())
# s = a.union(b)
# print(s.union(c))


# l = ['abx', 'sac', 'cag']
# s = set()
# for i in l:
#     s = s.union(i)
# print(s)


# with open('lesson-4/task5.txt', 'r+') as f:
#     s = set()
#     for line in f:
#         s = s.union(line[:-1])
#     print(s)


# with open('lesson-4/task6.txt', 'r+') as f:
#     for i in sorted(f):
#         f.write(i)


with open('lesson-4/tast7.txt', 'r+') as f:
    list = [line.split() for line in f]
    l1 = [int(i) for i in list[0]]
    s = max(l1)
    print(s)

with open('lesson-4/tast7.txt', 'w') as f:
    l1.remove(s)
    f.write(f"{str(l1)}")




