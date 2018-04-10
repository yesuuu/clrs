import numpy as np
import random

def merge(originList, start, mid, end):
    xList = originList[start:mid] + [np.inf]
    yList = originList[mid:end] + [np.inf]
    zList = []
    idxX, idxY = 0, 0
    for i in range(len(xList + yList) - 2):
        x, y = xList[idxX], yList[idxY]
        if x < y:
            zList.append(x)
            idxX += 1
        else:
            zList.append(y)
            idxY += 1
    originList[start:end] = zList
    return originList

def mergeSort(xList, start=0, end=None):
    if end is None:
        end = len(xList)
    if start < end - 1:
        mid = int((start + end) / 2.)
        mergeSort(xList, start, mid)
        mergeSort(xList, mid, end)
        xList = merge(xList, start, mid, end)
    return xList


if __name__ == '__main__':
    print mergeSort([1, ])
    print mergeSort([2, 1])
    print mergeSort([2, 2, 1])
    print mergeSort([2, 3, 4, 1])
    print mergeSort([1, 2, 4, 3])
    randomList = range(10)
    random.shuffle(randomList)
    print 'random:', randomList
    print mergeSort(randomList)

