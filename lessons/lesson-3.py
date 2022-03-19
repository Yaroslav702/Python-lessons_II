def getSum(list):
    sum = 0
    for i in list:
        if type(i) == int:
            sum += i
        else:
            continue
    return sum


def reverseList(lst):
    return lst[::-1]

def reverseList2(lst):
    return list(reversed(lst))


def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


def maxOfList(list):
    list_of_numbers = []
    for i in list:
        if type(i) == int:
            list_of_numbers.append(i)

    return max(list_of_numbers)


def getNumberOfUniqe(list):
    return len(set(list))


from collections import Counter, defaultdict
def getNumberOfElement(list):
    return Counter(list)

def getNumberOfElement2(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def getNumberOfElement3(list):
    d = defaultdict(int)
    for i in list:
        d[i] += 1
    return d


def getSameElements(l1, l2):
    return set(l1).intersection(set(l2))

def getSameElements2(l1,l2):
    intersection = []
    c1 = Counter(l1)
    c2 = Counter(l2)
    for k, val in c1.items():
        if k in c2.keys():
            intersection += [k] * min(val, c2[k])
    return intersection

         
def getNumberOfItem(l, k):
    count = 0
    for row in l:
        for item in row:
            if item == k:
                count += 1
    return count

def sumOfNumbers(two_dm_arr):
    sum = 0
    for row in two_dm_arr:
        for item in row:
            if type(item) == int:
                sum += item
    return sum


def mostCommonNumber(lst):
    c = Counter(lst).most_common(1)
    return c[0][0] 

print(mostCommonNumber([1,1,1,3]))








        


