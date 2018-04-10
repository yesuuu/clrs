class MaxHeap(object):

    def __init__(self, initList):
        self.heap = initList[:]
        self.length = len(initList)
        self.heapLength = len(initList)

        self.construct()

    def leftChild(self, i):
        leftIndex = 2 * i + 1
        return leftIndex if leftIndex < self.length else -1

    def rightChild(self, i):
        rightIndex = 2 * i + 2
        return rightIndex if rightIndex < self.length else -1

    def keepMax(self, i):
        # print i, self.heap[i]
        while True:
            left = self.leftChild(i)
            right = self.rightChild(i)
            if left >= 0 and left < self.heapLength and self.heap[i] < self.heap[left]:
                if right >= 0 and right < self.heapLength and self.heap[left] < self.heap[right]:
                    self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                    i = right
                else:
                    self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                    i = left
            elif right >= 0 and right < self.heapLength and self.heap[i] < self.heap[right]:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right
            else:
                break
        # print self.heap[:self.heapLength]

    def construct(self):
        for i in reversed(range((self.heapLength + 1) / 2)):
            self.keepMax(i)

    def removeMax(self):
        self.heap[0], self.heap[self.heapLength - 1] = self.heap[self.heapLength - 1], self.heap[0]
        self.heapLength -= 1
        return self



def heapSort(xList):
    returnList = []
    heap = MaxHeap(xList)
    for i in range(heap.length):
        max = heap.heap[0]
        heap.removeMax()
        heap.keepMax(0)
        returnList.append(max)
    return list(reversed(returnList))

if __name__ == '__main__':
    import random
    print heapSort([1, ])
    print heapSort([2, 1])
    print heapSort([2, 2, 1])
    print heapSort([2, 3, 4, 1])
    print heapSort([1, 2, 4, 3])
    randomList = range(10)
    random.shuffle(randomList)
    print 'random:', randomList
    print heapSort(randomList)

