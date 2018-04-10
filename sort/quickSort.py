import random

def quickSort(xList, start=0, end=None):

    if end is None:
        end = len(xList) - 1

    if end <= start:
        return xList

    if end-start >= 1:
        # print 'ooo', xList, start, end
        xList, q = frac(xList, start, end)
        # print 'aaa', xList, q
        xList = quickSort(xList, start, q-1)
        xList = quickSort(xList, q+1, end)
    return xList


def frac(xList, start, end):
    x = xList[end]
    i = start
    # print 'x', x
    for j in range(start, end):
        # print 'xList', xList
        # print 'j', j
        if xList[j] < x:
            xList[i], xList[j] = xList[j], xList[i]
            i += 1
    xList[i], xList[end] = x, xList[i]
    return xList, i



if __name__ == '__main__':
    print quickSort([1, ])
    print quickSort([2, 1])
    print quickSort([2, 2, 1])
    print quickSort([2, 3, 4, 1])
    print quickSort([1, 2, 4, 3])
    randomList = range(10)
    random.shuffle(randomList)
    print 'random:', randomList
    print quickSort(randomList)
