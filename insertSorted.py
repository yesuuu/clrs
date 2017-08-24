import random

def insertSorted(xList):
    n = len(xList)
    for sortIdx in range(1, n):
        cache = xList[sortIdx]
        idx = sortIdx - 1
        while idx >= 0 and xList[idx] > cache:
            xList[idx+1] = xList[idx]
            idx -= 1
        xList[idx+1] = cache
    return xList

if __name__ == '__main__':
    print insertSorted([1, ])
    print insertSorted([2, 1])
    print insertSorted([2, 2, 1])
    print insertSorted([2, 3, 4, 1])
    print insertSorted([1, 2, 4, 3])
    randomList = range(10)
    random.shuffle(randomList)
    print 'random:', randomList
    print insertSorted(randomList)

